import click
import dvc.api
import mlflow
import mlflow.xgboost
import pandas as pd
import numpy as np
import xgboost as xgb

from src.data import read_data, split_dataset
from src.logger import log

TRACKING_SERVER_HOST = "http://100.26.39.17:5000"
mlflow.set_tracking_uri(TRACKING_SERVER_HOST)
mlflow.set_experiment("prediccion-precios-casas")
mlflow.xgboost.autolog(importance_types=["gain"], model_format="json")


@click.command()
@click.option("--path", "-p", required=True, type=click.Path(exists=True))
@click.option("--label", "-l", default="SalePrice")
@click.option("--test-size", "-t", default=0.2)
@click.option("--seed", "-s", default=1399)
@click.option("--experiment-name", "-e", required=True)
@click.option("--nfold", "-n", default=5)
def main(path, label, test_size, seed, experiment_name, nfold):
    data_url = dvc.api.get_url(path=path, remote="myremote")
    feature_selector = [
        'Neighborhood', 'BldgType', 'OverallQual', 'OverallCond',
        'RoofMatl', 'BsmtQual', 'BsmtFinSF1', 'TotalBsmtSF', 'GrLivArea',
        'KitchenQual', 'GarageType', 'GarageCars'
    ]

    data = read_data(path)

    X_train, X_test, y_train, y_test = split_dataset(
        data=data, target=label, test_size=test_size, seed=seed
    )
    y_train, y_test = np.log(y_train), np.log(y_test)
    X_train, X_test = X_train[feature_selector], X_test[feature_selector]

    # <preprocesamiento>
    from category_encoders import TargetEncoder
    from sklearn.impute import KNNImputer
    from sklearn.pipeline import make_pipeline

    encoder = TargetEncoder()
    imputer = KNNImputer(n_neighbors=10, weights='distance')
    featurizer = make_pipeline(encoder, imputer)
    featurizer.fit(X_train, y_train)

    X_train = pd.DataFrame(
        featurizer.transform(X_train),
        columns=featurizer.get_feature_names_out()
    )
    X_test = pd.DataFrame(
        featurizer.transform(X_test),
        columns=featurizer.get_feature_names_out()
    )
    # </preprocesamiento>

    enable_categorical = (
        True if any(X_train.select_dtypes("category").columns.tolist()) else False
    )
    dtrain = xgb.DMatrix(
        data=X_train,
        label=y_train,
        feature_names=X_train.columns.tolist(),
        enable_categorical=enable_categorical,
    )
    dtest = xgb.DMatrix(
        data=X_test,
        label=y_test,
        feature_names=X_test.columns.tolist(),
        enable_categorical=enable_categorical,
    )

    with mlflow.start_run(experiment_id=1, run_name=experiment_name) as run:
        params = {
            "max_depth": 70,
            "min_child_weight": 1.5481359796122345,
            "reg_alpha": 1e-05,
            "reg_lambda": 1,
            'gamma': 0.018107780248991318,
            'colsample_bytree': 0.6,
            'subsample': 0.6,
            'eta': 0.056536933784715235,
            "objective": "reg:squarederror",
            "tree_method": "hist",
            "device": "cuda",
            "eval_metric": ["rmse", "mae"],
            "verbosity": 1,
            "seed": seed,
        }
        mlflow.log_params(
            {
                "data_url": data_url,
                "nfold": nfold,
                "enable_categorical": enable_categorical,
            }
        )
        # <log preprocesamiento>
        mlflow.log_param("encoder", "OrdinalEncoder")
        mlflow.sklearn.log_model(featurizer, "category_transformer")
        # </log preprocesamiento>

        log.info(f"Realizando CV (folds={nfold}) ... ")
        cv_results = xgb.cv(
            params=params,
            dtrain=dtrain,
            nfold=5,
            num_boost_round=500,
            early_stopping_rounds=10,
            verbose_eval=100,
            show_stdv=False,
        )

        for metric in params["eval_metric"]:
            best_iter = cv_results[f"test-{metric}-mean"].idxmin()
            mlflow.log_metric(
                f"cv-{metric}", cv_results[f"test-{metric}-mean"][best_iter]
            )

        log.info("Entrenando ...")
        model = xgb.train(
            params=params,
            dtrain=dtrain,
            evals=[(dtrain, "train"), (dtest, "eval")],
            early_stopping_rounds=10,
            num_boost_round=500,
            verbose_eval=100,
        )

        if not enable_categorical:
            log.info("Evaluando (mlflow)...")
            mlflow.evaluate(
                model=f"runs:/{run.info.run_id}/model",
                data=X_test.values,
                targets=y_test.values,
                predictions=model.predict(dtest),
                feature_names=X_test.columns.tolist(),
                model_type="regressor",
            )


if __name__ == "__main__":
    main()

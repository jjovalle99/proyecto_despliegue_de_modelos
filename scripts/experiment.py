import click
import dvc.api
import mlflow
import mlflow.xgboost
import xgboost as xgb

from src.data import read_data, split_dataset, categorical_encoding
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

    data = read_data(path)
    X_train, X_test, y_train, y_test = split_dataset(data=data, target=label,
                                                     test_size=test_size,
                                                     seed=seed)

    # <preprocesamiento>
    from sklearn.preprocessing import OrdinalEncoder
    import numpy as np
    encoder = OrdinalEncoder(
        handle_unknown='use_encoded_value',
        unknown_value=np.nan
    )
    X_train, X_test, transformer = categorical_encoding(encoder=encoder, X_train=X_train,
                                                        X_test=X_test)
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
            "eta": 0.01,
            "objective": "reg:squarederror",
            "tree_method": "hist",
            "device": "cuda",
            "eval_metric": ["rmse", "mae"],
            # "nthread": 24,
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
        mlflow.log_param('encoder', 'OrdinalEncoder')
        mlflow.sklearn.log_model(transformer, "category_transformer")
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

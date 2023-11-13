import click
import dvc.api
import mlflow
import mlflow.xgboost
import xgboost as xgb
from sklearn.model_selection import train_test_split

from src.data import read_data

TRACKING_SERVER_HOST = "http://100.26.39.17:5000"
mlflow.set_tracking_uri(TRACKING_SERVER_HOST)
mlflow.set_experiment("prediccion-precios-casas")


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
    X, y = data.drop(label, axis=1), data[label]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, shuffle=True, random_state=seed
    )

    mlflow.xgboost.autolog(importance_types=["gain"], model_format="json")
    enable_categorical = (
        True if any(X.select_dtypes("category").columns.tolist()) else False
    )
    dtrain = xgb.DMatrix(
        data=X_train,
        label=y_train,
        feature_names=X.columns.tolist(),
        enable_categorical=enable_categorical,
    )
    dtest = xgb.DMatrix(
        data=X_test,
        label=y_test,
        feature_names=X.columns.tolist(),
        enable_categorical=enable_categorical,
    )

    with mlflow.start_run(experiment_id=1, run_name=experiment_name):
        params = {
            "eta": 0.01,
            "objective": "reg:squarederror",
            "tree_method": "hist",
            "eval_metric": ["rmse", "mae"],
            "nthread": 8,
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
        print(f"Realizando CV (folds={nfold}) ... ")
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

        print("Entrenando ...")
        xgb.train(
            params=params,
            dtrain=dtrain,
            evals=[(dtrain, "train"), (dtest, "eval")],
            early_stopping_rounds=10,
            num_boost_round=500,
            verbose_eval=100,
        )


if __name__ == "__main__":
    main()

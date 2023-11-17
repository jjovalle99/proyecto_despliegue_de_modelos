from typing import Any

import mlflow
import numpy as np
import pandas as pd

from src.logger import log


def load_model_from_mlflow(run_id: str, model_name: str = "model") -> Any:
    """
    Se carga un modelo desde Mlflow.
    """
    log.info(f"Cargando modelo [{model_name}] del run [{run_id}] desde Mlflow ...")
    try:
        model_uri = f"runs:/{run_id}/{model_name}"
        model = mlflow.pyfunc.load_model(model_uri)
    except Exception as e:
        log.error(f"Error al cargar modelo desde Mlflow: {e}")
        raise

    return model


def generate_predictions_model_mlflow(model: Any, data: pd.DataFrame) -> np.ndarray:
    """
    Se generan predicciones con un modelo cargado desde Mlflow.
    """
    log.info("Generando predicciones ...")
    try:
        results = model.predict(data)
    except Exception as e:
        log.error(f"Error al generar predicciones: {e}")
        raise

    return results

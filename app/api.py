from pathlib import Path

import mlflow
import numpy as np
import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.logger import log
from src.model import generate_predictions_model_mlflow
from src.schema import Input, Prediction

MODELS_PATH = Path.cwd() / "models"

app = FastAPI(title="Prediccion de precios de casas.", version="0.1.1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def hello():
    return {"message": "Esta es un API para predecir precios de casas."}


@app.post("/predict", response_model=Prediction)
def predict(house_data: Input):
    try:
        log.info("Cargando modelos ...")
        transformer = mlflow.sklearn.load_model(MODELS_PATH / "category_transformer")
        model = mlflow.pyfunc.load_model(MODELS_PATH / "model")
    except Exception as e:
        log.error(f"Error al cargar modelos: {e}")
        raise

    try:
        data_df = pd.DataFrame([house_data.dict(by_alias=True)])
        data_df = pd.DataFrame(transformer.transform(data_df), columns=data_df.columns)
    except Exception as e:
        log.error(f"Error al preparar los datos: {e}")
        raise

    try:
        predictions = generate_predictions_model_mlflow(
            model=model, data=data_df
        ).tolist()
        return {"prediction": np.exp(predictions)}
    except Exception as e:
        log.error(f"Error al generar predicciones: {e}")
        raise


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=1399, log_level="debug")

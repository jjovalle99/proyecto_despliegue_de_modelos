import pandas as pd

from src.logger import log


def read_data(path: str) -> pd.DataFrame:
    """
    Lee datos de archivos de entrenamiento, luego dropea la columna `Id` y
    convierte las columnas de tipo `object` a tipo `category`.
    """
    log.info(f"Leyendo datos de {path} ...")

    try:
        # Se leen los datos
        data = pd.read_csv(path)

        # Si la columna `Id` existe, se elimina
        if "Id" in data.columns:
            data.drop("Id", axis=1, inplace=True)

        log.info("Datos leídos correctamente.")
    except Exception as e:
        log.error(f"Error al leer los datos: {e}")
        raise

    # Se convierten las columnas de tipo `object` a tipo `category`
    try:
        object_cols = data.select_dtypes(include="object").columns
        data[object_cols] = data[object_cols].astype("category")
    except Exception as e:
        log.error(f"Error al convertir columnas a tipo `category`: {e}")

    return data

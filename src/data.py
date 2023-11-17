import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.base import BaseEstimator
from sklearn.compose import make_column_transformer
from typing import Tuple

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


def split_dataset(data: pd.DataFrame, target: str, test_size: float = 0.2, seed: int = 1399
                  ) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """
    Primero se separan los datos en `X` y `y`, luego se separan en datos de entrenamiento y
    prueba.
    """
    log.info("Separando datos en entrenamiento y prueba ...")
    try:
        X, y = data.drop(target, axis=1), data[target]
    except Exception as e:
        log.error(f"Error al separar los datos: {e}")
        raise

    try:
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, shuffle=True, random_state=seed
        )
    except Exception as e:
        log.error(f"Error al separar los datos en entrenamiento y prueba: {e}")
        raise

    return X_train, X_test, y_train, y_test


def categorical_encoding(encoder: BaseEstimator, X_train: pd.DataFrame, X_test: pd.DataFrame,
                         verbose: int = 1, n_jobs: int = -1
                         ) -> Tuple[pd.DataFrame, pd.DataFrame, BaseEstimator]:
    """
    Dado un encoder, se transforman las columnas categóricas de los datos de entrenamiento y
    prueba.
    """
    log.info("Transformando columnas categóricas ...")
    # Se obtienen los nombres de las columnas categóricas
    categorical_columns_list = X_train.select_dtypes(include="category").columns.to_list()

    # Se construye un `ColumnTransformer` que transforma las columnas categóricas
    transformer = make_column_transformer(
        (encoder, categorical_columns_list),
        remainder="passthrough",
        verbose_feature_names_out=False,
        verbose=verbose,
        n_jobs=n_jobs,
    )

    try:
        # Se ajusta el encoder-transformer
        transformer.fit(X_train)
    except Exception as e:
        log.error(f"Error al entrenar el encoder: {e}")
        raise

    try:
        # Se crean dataframes con los datos transformados
        X_train = pd.DataFrame(
            transformer.transform(X_train),
            columns=transformer.get_feature_names_out(),
            index=X_train.index,
        )
        X_test = pd.DataFrame(
            transformer.transform(X_test),
            columns=transformer.get_feature_names_out(),
            index=X_test.index,
        )
    except Exception as e:
        log.error(f"Error al transformar los datos: {e}")
        raise

    return X_train, X_test, transformer

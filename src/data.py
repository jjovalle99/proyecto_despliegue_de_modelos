import pandas as pd


def read_data(path):
    data = pd.read_csv(path)

    if "Id" in data.columns:
        data.drop("Id", axis=1, inplace=True)

    object_cols = data.select_dtypes(include="object").columns
    data[object_cols] = data[object_cols].astype("category")

    return data

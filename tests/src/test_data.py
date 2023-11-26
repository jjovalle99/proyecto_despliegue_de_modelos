import pandas as pd
import pytest
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

from src.data import categorical_encoding, read_data, split_dataset


def test_read_data_success():
    test_path = "data/train.csv"
    result = read_data(test_path)

    assert isinstance(result, pd.DataFrame)
    assert "Id" not in result.columns
    assert all(
        dtype.name == "category" for dtype in result.dtypes[result.dtypes == "object"]
    )


def test_read_data_file_not_found():
    with pytest.raises(Exception):
        read_data("non_existent_file.csv")


def test_split_dataset():
    data = pd.DataFrame(
        {"feature1": range(100), "feature2": range(100, 200), "target": range(200, 300)}
    )
    target = "target"
    test_size = 0.2

    X_train, X_test, y_train, y_test = split_dataset(data, target, test_size=test_size)

    assert len(X_train) == 80
    assert len(X_test) == 20
    assert len(y_train) == 80
    assert len(y_test) == 20

    assert target not in X_train.columns
    assert target not in X_test.columns


def test_categorical_encoding():
    encoder = OneHotEncoder()

    X_train = pd.DataFrame(
        {"cat_feature": ["A", "B", "A", "C"], "num_feature": [1, 2, 3, 4]}
    )
    X_test = pd.DataFrame(
        {"cat_feature": ["B", "A", "C", "C"], "num_feature": [5, 6, 7, 8]}
    )

    X_train["cat_feature"] = X_train["cat_feature"].astype("category")
    X_test["cat_feature"] = X_test["cat_feature"].astype("category")

    X_train_transformed, X_test_transformed, transformer = categorical_encoding(
        encoder, X_train, X_test
    )

    assert X_train_transformed.shape[1] > X_train.shape[1]
    assert X_test_transformed.shape[1] > X_test.shape[1]
    assert isinstance(transformer, ColumnTransformer)
    assert all(col in X_train_transformed.columns for col in X_test_transformed.columns)

import pytest

from src.schema import Input, Prediction


def test_prediction_instantiation():
    pred = Prediction(prediction=1.23)
    assert pred.prediction == 1.23

    pred = Prediction(prediction=[1.23, 4.56])
    assert pred.prediction == [1.23, 4.56]


def test_prediction_validation():
    with pytest.raises(ValueError):
        Prediction(prediction="invalid")


def test_input_instantiation():
    example = {
        "Neighborhood": "CollgCr",
        "BldgType": "1Fam",
        "OverallQual": 7,
        "OverallCond": 5,
        "RoofMatl": "CompShg",
        "BsmtQual": "Gd",
        "BsmtFinSF1": 706,
        "TotalBsmtSF": 856,
        "GrLivArea": 1710,
        "KitchenQual": "Gd",
        "GarageType": "Attchd",
        "GarageCars": 2,
    }
    input_data = Input(**example)
    assert input_data.dict() == example


def test_input_optional_fields():
    data = {
        "Neighborhood": "CollgCr",
        "BldgType": "1Fam",
        "OverallQual": 7,
        "OverallCond": 5,
        "RoofMatl": "CompShg",
        "BsmtFinSF1": 706,
        "TotalBsmtSF": 856,
        "GrLivArea": 1710,
        "KitchenQual": "Gd",
        "GarageCars": 2,
    }
    input_data = Input(**data)
    assert input_data.BsmtQual is None
    assert input_data.GarageType is None

from typing import List, Optional

from pydantic import BaseModel, Field


class Prediction(BaseModel):
    prediction: List[float] | float


class Input(BaseModel):
    MSSubClass: int
    MSZoning: str
    LotFrontage: Optional[float]
    LotArea: int
    Street: str
    Alley: Optional[str]
    LotShape: str
    LandContour: str
    Utilities: str
    LotConfig: str
    LandSlope: str
    Neighborhood: str
    Condition1: str
    Condition2: str
    BldgType: str
    HouseStyle: str
    OverallQual: int
    OverallCond: int
    YearBuilt: int
    YearRemodAdd: int
    RoofStyle: str
    RoofMatl: str
    Exterior1st: str
    Exterior2nd: str
    MasVnrType: Optional[str]
    MasVnrArea: Optional[float]
    ExterQual: str
    ExterCond: str
    Foundation: str
    BsmtQual: Optional[str]
    BsmtCond: Optional[str]
    BsmtExposure: Optional[str]
    BsmtFinType1: Optional[str]
    BsmtFinSF1: int
    BsmtFinType2: Optional[str]
    BsmtFinSF2: int
    BsmtUnfSF: int
    TotalBsmtSF: int
    Heating: str
    HeatingQC: str
    CentralAir: str
    Electrical: Optional[str]
    FirstFlrSF: int = Field(..., alias="1stFlrSF")
    SecondFlrSF: int = Field(..., alias="2ndFlrSF")
    LowQualFinSF: int
    GrLivArea: int
    BsmtFullBath: int
    BsmtHalfBath: int
    FullBath: int
    HalfBath: int
    BedroomAbvGr: int
    KitchenAbvGr: int
    KitchenQual: str
    TotRmsAbvGrd: int
    Functional: str
    Fireplaces: int
    FireplaceQu: Optional[str]
    GarageType: Optional[str]
    GarageYrBlt: Optional[float]
    GarageFinish: Optional[str]
    GarageCars: int
    GarageArea: int
    GarageQual: Optional[str]
    GarageCond: Optional[str]
    PavedDrive: str
    WoodDeckSF: int
    OpenPorchSF: int
    EnclosedPorch: int
    ThreeSsnPorch: int = Field(..., alias="3SsnPorch")
    ScreenPorch: int
    PoolArea: int
    PoolQC: Optional[str]
    Fence: Optional[str]
    MiscFeature: Optional[str]
    MiscVal: int
    MoSold: int
    YrSold: int
    SaleType: str
    SaleCondition: str

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "MSSubClass": 60,
                "MSZoning": "RL",
                "LotFrontage": 65.0,
                "LotArea": 8450,
                "Street": "Pave",
                "Alley": None,
                "LotShape": "Reg",
                "LandContour": "Lvl",
                "Utilities": "AllPub",
                "LotConfig": "Inside",
                "LandSlope": "Gtl",
                "Neighborhood": "CollgCr",
                "Condition1": "Norm",
                "Condition2": "Norm",
                "BldgType": "1Fam",
                "HouseStyle": "2Story",
                "OverallQual": 7,
                "OverallCond": 5,
                "YearBuilt": 2003,
                "YearRemodAdd": 2003,
                "RoofStyle": "Gable",
                "RoofMatl": "CompShg",
                "Exterior1st": "VinylSd",
                "Exterior2nd": "VinylSd",
                "MasVnrType": "BrkFace",
                "MasVnrArea": 196.0,
                "ExterQual": "Gd",
                "ExterCond": "TA",
                "Foundation": "PConc",
                "BsmtQual": "Gd",
                "BsmtCond": "TA",
                "BsmtExposure": "No",
                "BsmtFinType1": "GLQ",
                "BsmtFinSF1": 706,
                "BsmtFinType2": "Unf",
                "BsmtFinSF2": 0,
                "BsmtUnfSF": 150,
                "TotalBsmtSF": 856,
                "Heating": "GasA",
                "HeatingQC": "Ex",
                "CentralAir": "Y",
                "Electrical": "SBrkr",
                "1stFlrSF": 856,
                "2ndFlrSF": 854,
                "LowQualFinSF": 0,
                "GrLivArea": 1710,
                "BsmtFullBath": 1,
                "BsmtHalfBath": 0,
                "FullBath": 2,
                "HalfBath": 1,
                "BedroomAbvGr": 3,
                "KitchenAbvGr": 1,
                "KitchenQual": "Gd",
                "TotRmsAbvGrd": 8,
                "Functional": "Typ",
                "Fireplaces": 0,
                "FireplaceQu": None,
                "GarageType": "Attchd",
                "GarageYrBlt": 2003.0,
                "GarageFinish": "RFn",
                "GarageCars": 2,
                "GarageArea": 548,
                "GarageQual": "TA",
                "GarageCond": "TA",
                "PavedDrive": "Y",
                "WoodDeckSF": 0,
                "OpenPorchSF": 61,
                "EnclosedPorch": 0,
                "3SsnPorch": 0,
                "ScreenPorch": 0,
                "PoolArea": 0,
                "PoolQC": None,
                "Fence": None,
                "MiscFeature": None,
                "MiscVal": 0,
                "MoSold": 2,
                "YrSold": 2008,
                "SaleType": "WD",
                "SaleCondition": "Normal",
                "SalePrice": 208500,
            }
        }
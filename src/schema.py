from typing import List, Optional

from pydantic import BaseModel


class Prediction(BaseModel):
    prediction: List[float] | float


class Input(BaseModel):
    Neighborhood: str
    BldgType: str
    OverallQual: int
    OverallCond: int
    RoofMatl: str
    BsmtQual: Optional[str]
    BsmtFinSF1: int
    TotalBsmtSF: int
    GrLivArea: int
    KitchenQual: str
    GarageType: Optional[str]
    GarageCars: int

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
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
        }

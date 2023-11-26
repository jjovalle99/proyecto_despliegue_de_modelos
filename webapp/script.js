function enviarFormulario() {
    var OverallQual = document.getElementById('OverallQual').value;
    var OverallCond = document.getElementById('OverallCond').value;
    var YearBuilt = document.getElementById('YearBuilt').value;
    var TotalBsmtSF = document.getElementById('TotalBsmtSF').value;
    var GarageCars = document.getElementById('GarageCars').value;
    var GarageArea = document.getElementById('GarageArea').value;
    var FirstFlrSF = document.getElementById('FirstFlrSF').value;
    var SecondFlrSF = document.getElementById('SecondFlrSF').value;

    var data_ejemplo_consumo_api = {
      "MSSubClass": 60,
      "MSZoning": "RL",
      "LotFrontage": 65,
      "LotArea": 8450,
      "Street": "Pave",
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
      "OverallQual": OverallQual,
      "OverallCond": OverallCond,
      "YearBuilt": YearBuilt,
      "YearRemodAdd": 2003,
      "RoofStyle": "Gable",
      "RoofMatl": "CompShg",
      "Exterior1st": "VinylSd",
      "Exterior2nd": "VinylSd",
      "MasVnrType": "BrkFace",
      "MasVnrArea": 196,
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
      "TotalBsmtSF": TotalBsmtSF,
      "Heating": "GasA",
      "HeatingQC": "Ex",
      "CentralAir": "Y",
      "Electrical": "SBrkr",
      "1stFlrSF": FirstFlrSF,
      "2ndFlrSF": SecondFlrSF,
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
      "GarageType": "Attchd",
      "GarageYrBlt": 2003,
      "GarageFinish": "RFn",
      "GarageCars": GarageCars,
      "GarageArea": GarageArea,
      "GarageQual": "TA",
      "GarageCond": "TA",
      "PavedDrive": "Y",
      "WoodDeckSF": 0,
      "OpenPorchSF": 61,
      "EnclosedPorch": 0,
      "3SsnPorch": 0,
      "ScreenPorch": 0,
      "PoolArea": 0,
      "MiscVal": 0,
      "MoSold": 2,
      "YrSold": 2008,
      "SaleType": "WD",
      "SaleCondition": "Normal",
      "SalePrice": 208500
    };

    var xhr = new XMLHttpRequest();
    var url = "http://ec2-3-227-189-106.compute-1.amazonaws.com:1399/predict";
    // var url = "https://a580fec5-d7a9-47d7-b885-4e39fef37b0c.mock.pstmn.io/predict";
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
      if (xhr.readyState === 4 && xhr.status === 200) {
        var json = JSON.parse(xhr.responseText);
        document.getElementById('respuesta').textContent = JSON.stringify(json);
        console.log('Respuesta del servidor:', json);
        var respuesta = document.getElementById('respuesta');
        // Accede a la propiedad 'prediction' y toma el primer elemento del array
        var valor = json.prediction[0];
        respuesta.value = '$ ' + valor.toLocaleString('en-US') + ' USD';
      }
    };


    var data = JSON.stringify(data_ejemplo_consumo_api);
    console.log('Datos enviados al servidor:', data);
    xhr.send(data);
  }

  document.addEventListener('DOMContentLoaded', (event) => {
    document.getElementById('calcular').addEventListener('click', enviarFormulario);
    });
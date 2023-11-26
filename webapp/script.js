function enviarFormulario() {
    var Neighborhood = document.getElementById('Neighborhood').value;
    var OverallQual = document.getElementById('OverallQual').value;
    var OverallCond = document.getElementById('OverallCond').value;
    var BldgType = document.getElementById('BldgType').value;
    var RoofMatl = document.getElementById('RoofMatl').value;
    var GarageCars = document.getElementById('GarageCars').value;
    var BsmtQual = document.getElementById('BsmtQual').value;
    var BsmtFinSF1 = document.getElementById('BsmtFinSF1').value;
    var TotalBsmtSF = document.getElementById('TotalBsmtSF').value;
    var GrLivArea = document.getElementById('GrLivArea').value;
    var KitchenQual = document.getElementById('KitchenQual').value;
    var GarageType = document.getElementById('GarageType').value;

    var data_ejemplo_consumo_api = {
      "Neighborhood": Neighborhood,
      "BldgType": BldgType,
      "OverallQual": OverallQual,
      "OverallCond": OverallCond,
      "RoofMatl": RoofMatl,
      "BsmtQual": BsmtQual,
      "BsmtFinSF1": BsmtFinSF1,
      "TotalBsmtSF": TotalBsmtSF,
      "GrLivArea": GrLivArea,
      "KitchenQual": KitchenQual,
      "GarageType": GarageType,
      "GarageCars": GarageCars
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
        var valor = json.prediction;
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
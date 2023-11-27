
# Dashboard de Predicción de Precios de Casas
## Acceso al Dashboard
El dashboard está disponible en la siguiente dirección: [Dashboard en AWS](http://ec2-44-219-17-49.compute-1.amazonaws.com:8000/). En este dashboard podrás encontrar
- Información descriptiva sobre casas, incluyendo características y precios.
- Un modelo interactivo para predecir el precio de venta de una casa basado en características específicas ingresadas por el usuario.
- Acceso a los experimentos de MLflow utilizados para desarrollar el modelo.
  
![image](https://github.com/jjovalle99/proyecto_despliegue_de_modelos/assets/70274018/cc7ac825-411e-4567-859f-0f3f2ef7de1b)

## Evidencia de Arquitectura en AWS
![image](https://github.com/jjovalle99/proyecto_despliegue_de_modelos/assets/70274018/994abbf6-1cf8-47ea-bd7c-754f3012a4e8)

## Manual de despliegue del modelo
### Requisitos
- Git
- Docker

### Pasos para el despliegue

#### 1. Clonar el Repositorio
```bash
git clone https://github.com/jjovalle99/proyecto_despliegue_de_modelos.git
```

#### 2. Construir la Imagen con Docker
```bash
cd proyecto_despliegue_de_modelos
docker build -t prediccion-casas:latest .
docker run --rm -p 1399:1399 prediccion-casas:latest 
```

#### 3. Verificar el Despliegue del Modelo
Una vez completados los pasos anteriores, puedes acceder a la documentación del API en la ruta localhost:1399/docs.

#### 4. Probar el Modelo
El modelo se puede probar directamente desde la documentación o mediante la terminal con el siguiente comando:
```bash
curl -X 'POST' \
  'http://localhost:1399/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
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
  "GarageCars": 2
}'
```

#### 5. Opción de Alojamiento en la Nube
Para un despliegue en la nube, se recomienda una instancia t2.micro con 10 GB de almacenamiento y sistema operativo Ubuntu. Los pasos son similares a los anteriores. Asegúrate de instalar Docker ([Instrucciones de instalación](https://docs.docker.com/engine/install/ubuntu/)) y abrir el tráfico al puerto 1399.

## Manual de despliegue del Dashboard
Para desplegar el dashboard, dirígete a la subcarpeta webapp y sigue las instrucciones proporcionadas allí.

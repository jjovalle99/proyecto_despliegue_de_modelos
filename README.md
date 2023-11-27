# Manual de despliegue del modelo
Para desplegar el modelo se necesita: 
- Git
- Docker

#### 1. Se clona el repositorio
```bash
git clone https://github.com/jjovalle99/proyecto_despliegue_de_modelos.git
```

#### 2. Se construye la imagen apartir del Dockerfile
```bash
cd proyecto_despliegue_de_modelos
docker build -t prediccion-casas:latest .
docker run --rm -p 1399:1399 prediccion-casas:latest 
```

#### 3. Verificar que el modelo se desplegara
Si los pasos fueron ejecutados correctamente, podra entrar a la documentacion
del API en la ruta `localhost:1399/docs`

#### 4. Pruebe el modelo
Puede probar el modelo directamente en la documentacion o llamarlo desde la terminal de la
siguiente manera:
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

# Evidencia 
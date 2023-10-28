
# Cómo instalar el entorno

Para instalar el gestor de dependencias Poetry:
```bash
pip install poetry
poetry config virtualenvs.in-project true
```

Para instalar el entorno apartir de los archivos `pyproject.toml` y `poetry.lock`
```bash
poetry install
```

Para activar el entorno
```bash
poetry shell
```

# Descargar los datos del remoto

Para descargar los datos desde el remoto (S3) configurar las credenciales en `~/.aws/credentials` y luego ejecutar:
```
dvc pull -r myremote
```
En caso de manejar diferentes perfiles de AWS, asegurarse de configuarlo de la siguiente manera:
```
export AWS_PROFILE=<nombre del perfil>
```

# Prueba PR Gabriel no, Prueba Diego

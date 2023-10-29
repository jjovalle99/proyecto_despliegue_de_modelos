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

# Arquitectura
![image](https://github.com/jjovalle99/proyecto_despliegue_de_modelos/assets/70274018/a52c7e3d-c448-483b-b5ca-9b255a73371b)

# Bosquejo del producto final
![image](https://github.com/jjovalle99/proyecto_despliegue_de_modelos/assets/70274018/427f56e6-3cf2-4cf4-8342-988d4358ac60)

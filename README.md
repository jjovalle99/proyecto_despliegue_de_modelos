# Cómo instalar el entorno
Se recomienda usar miniconda, el cual puede descargar en https://docs.conda.io/projects/miniconda/en/latest/
![image](https://github.com/jjovalle99/proyecto_despliegue_de_modelos/assets/70274018/5713fe31-ea0c-4710-9a69-5efeaf165786)

Una vez instalado miniconda, puede crear un ambiente usando:
```
conda create -n ambiente_proyecto python=3.10 pip
```

Cuando se cree el ambiente, activelo usando:
```
conda activate ambiente_proyecto
```

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

# Descargar los datos desde el remoto (S3)
Obtenga sus credenciales desde la pagina donde lanza su cuenta de AWS:
<img width="911" alt="Screenshot 2023-10-29 at 12 33 25 PM" src="https://github.com/jjovalle99/proyecto_despliegue_de_modelos/assets/70274018/a6ad4b22-29fb-4c5b-bda9-5ba767ea5810">

Configure las credenciales de su cuenta de AWS de la siguiente manera:
## En Windows
```
set AWS_ACCESS_KEY_ID=<aws_access_key_id>
set AWS_SECRET_ACCESS_KEY=<aws_secret_access_key>
set AWS_SESSION_TOKEN=<aws_session_token>
```
## En macOS y Linux
```
export AWS_ACCESS_KEY_ID=<aws_access_key_id>
export AWS_SECRET_ACCESS_KEY=<aws_secret_access_key>
export AWS_SESSION_TOKEN=<aws_session_token>
```

Para descargar los datos ejecutar:
```
dvc pull -r myremote
```

_Nota: Este proceso lo tiene que hacer cada que vez que quiera descargar los datos desde el remoto.
Si quiere evitar repetir este proceso, configure sus credenciales en `~/.aws/credentials`.
En caso de que maneje diferentes perfiles de AWS, asegurarse de especificar el perfil correcto
usando `export AWS_PROFILE=<nombre del perfil>` (en macOS y Linux) o `set AWS_PROFILE=<nombre del perfil>` (en Windows)_

# Arquitectura
![image](https://github.com/jjovalle99/proyecto_despliegue_de_modelos/assets/70274018/a52c7e3d-c448-483b-b5ca-9b255a73371b)

# Bosquejo del producto final
![image](https://github.com/jjovalle99/proyecto_despliegue_de_modelos/assets/70274018/427f56e6-3cf2-4cf4-8342-988d4358ac60)

# URL Dashboard LookerStudio (Trabajo en progreso)
https://lookerstudio.google.com/reporting/208f117c-8536-47ba-9ec2-d963f357dfa1

# Servidor Mlflow: http://100.26.39.17:5000/
![image](https://github.com/jjovalle99/proyecto_despliegue_de_modelos/assets/70274018/51f98b74-5f23-4bb7-8a9c-a821e849f89c)


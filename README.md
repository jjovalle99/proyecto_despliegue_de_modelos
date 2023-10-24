
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
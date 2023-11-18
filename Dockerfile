FROM python:3.10.13-slim

ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /proyecto

COPY ./ ./

RUN touch README.md && \
pip install poetry==1.6.1 --no-cache-dir && \
poetry install --no-interaction --no-ansi --no-cache \
--without mlops --without ml --without dev --without test

EXPOSE 1399

ENTRYPOINT [ "uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "1399"]
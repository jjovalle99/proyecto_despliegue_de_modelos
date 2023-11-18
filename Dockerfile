FROM python:3.10.13-slim AS builder

RUN pip install poetry==1.6.1 --no-cache-dir

ENV POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 

WORKDIR /proyecto

COPY pyproject.toml poetry.lock ./
RUN touch README.md

RUN poetry install --no-interaction \
--no-ansi \
--no-cache \
--no-root \
--without mlops \
--without ml \
--without dev \
--without test 

FROM python:3.10.13-slim AS runtime

ENV VIRTUAL_ENV=/proyecto/.venv \
    PATH="/proyecto/.venv/bin:$PATH"

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

RUN useradd -M user
USER user

WORKDIR /proyecto

COPY --chown=user ./  ./ 

EXPOSE 1399

ENTRYPOINT [ "uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "1399"]
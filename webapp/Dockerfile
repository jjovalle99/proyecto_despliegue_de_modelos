FROM python:3.8-slim-buster
WORKDIR /app
COPY . /app
RUN pip install flask
EXPOSE 8000
CMD ["python", "webApp.py"]
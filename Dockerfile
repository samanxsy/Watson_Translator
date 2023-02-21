FROM python:3.10-alpine

WORKDIR /watson-translator

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY .dockerignore /

COPY ./app ./app

ENV API_KEY=$watson_API_KEY

CMD ["python", "-m", "app.server"]

EXPOSE 8000

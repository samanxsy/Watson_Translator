FROM python:3.10

WORKDIR /watson-translator

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app ./app

ENV API_KEY=$watson_API_KEY

CMD ["python", "./app/server.py"]
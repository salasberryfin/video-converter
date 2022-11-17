FROM python:3.8-slim

RUN apt-get clean && apt-get update -y

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY src/. .

EXPOSE 5000

CMD ["python", "api.py"]

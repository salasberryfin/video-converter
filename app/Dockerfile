FROM python:3.8-slim

RUN apt-get clean && apt-get update -y

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY src/. .

ENV FLASK_RUN_PORT=5000
ENV FLASK_DEBUG=True

EXPOSE 5000

CMD ["python", "api.py"]

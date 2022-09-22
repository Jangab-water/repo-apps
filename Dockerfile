FROM python:3.10-slim-buster

COPY app.py /app/app.py

RUN python3 -m pip install -r requirements.txt

ENTRYPOINT python3 app.py
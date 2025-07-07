FROM python:3.13-slim

ENV TZ=Europe/Warsaw

WORKDIR /app

COPY app.py .

RUN pip install Flask gunicorn

EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "6", "--access-logfile", "-", "--error-logfile", "-", "app:app"]


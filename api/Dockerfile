FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*

RUN useradd --create-home --shell /bin/bash appuser

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=appuser:appuser app.py .

ARG APP_VERSION=unknown

ENV APP_VERSION=$APP_VERSION

USER appuser

CMD ["python", "app.py"]

EXPOSE 8080

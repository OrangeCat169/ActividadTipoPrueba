FROM python:3.11-slim

WORKDIR /app

COPY app.py .


# Instala curl, cliente MySQL y paquetes de Python directamente
RUN apt-get update && apt-get install -y curl default-mysql-client && \
    pip install --no-cache-dir flask mysql-connector-python && \
    rm -rf /var/lib/apt/lists/*

CMD ["python", "app.py"]
# Usamos una imagen slim para reducir tamaño y superficie de ataque
FROM python:3.10-slim

# Evita que Python genere archivos .pyc y habilita logs en tiempo real
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Usamos CMD para ejecutar el script, Cloud Run inyectará la variable PORT
CMD ["python", "app.py"]
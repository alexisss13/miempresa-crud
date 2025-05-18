# Usa la imagen oficial de Python ligera
FROM python:3.11-slim

# Instala las librerías de sistema necesarias para mysqlclient
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev build-essential \
  && rm -rf /var/lib/apt/lists/*

# Crea y usa el directorio /app
WORKDIR /app
COPY . .

# Actualiza pip y instala dependencias de Python
RUN pip install --upgrade pip setuptools wheel \
 && pip install -r requirements.txt

# Expón el puerto (opcional, Railway lo detecta)
EXPOSE 8000

# Comando por defecto: migra y arranca Gunicorn
CMD ["sh", "-c", "python manage.py migrate && gunicorn miempresa.wsgi --bind 0.0.0.0:8000"]

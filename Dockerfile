# Dockerfile
FROM python:3.11-slim

# Instala librerías de sistema para mysqlclient y Pillow
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    default-libmysqlclient-dev \
    libjpeg-dev \
    zlib1g-dev \
    libfreetype6-dev \
    liblcms2-dev \
    libopenjp2-7-dev \
    libtiff5-dev \
 && rm -rf /var/lib/apt/lists/*

# Copia código y fija working dir
WORKDIR /app
COPY . .

# Instala dependencias Python
RUN pip install --upgrade pip setuptools wheel \
 && pip install -r requirements.txt

# Expone puerto (opcional)
EXPOSE 8000

# Al arrancar: migraciones + Gunicorn
CMD ["sh", "-c", "python manage.py migrate && gunicorn miempresa.wsgi --bind 0.0.0.0:8000"]

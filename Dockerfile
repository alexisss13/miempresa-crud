# Dockerfile
FROM python:3.11-slim

# 1) Instala dependencias de sistema para mysqlclient y Pillow:
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \             # gcc, make, etc.
    python3-dev \                 # cabeceras de Python para compilar extensiones C
    default-libmysqlclient-dev \   # cliente MySQL
    libjpeg-dev \                 # JPEG para Pillow
    zlib1g-dev \                  # zlib para Pillow
    libfreetype6-dev \            # font support
    liblcms2-dev \                # color management
    libopenjp2-7-dev \            # JPEG2000
    libtiff5-dev \                # TIFF
  && rm -rf /var/lib/apt/lists/*

# 2) Copia el código al contenedor
WORKDIR /app
COPY . .

# 3) Actualiza pip y instala dependencias Python
RUN pip install --upgrade pip setuptools wheel \
 && pip install -r requirements.txt

# 4) Expone el puerto 8000 (Railway lo detecta automáticamente)
EXPOSE 8000

# 5) Al arrancar: aplica migraciones y levanta Gunicorn
CMD ["sh", "-c", "python manage.py migrate && gunicorn miempresa.wsgi --bind 0.0.0.0:8000"]

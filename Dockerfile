# Dockerfile
FROM python:3.11-slim

# Instala librerías C necesarias para mysqlclient y Pillow
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    default-libmysqlclient-dev \
    pkg-config \             # <— necesario para mysqlclient
    libjpeg-dev \
    zlib1g-dev \
    libfreetype6-dev \
    liblcms2-dev \
    libopenjp2-7-dev \
    libtiff5-dev \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .

RUN pip install --upgrade pip setuptools wheel \
 && pip install -r requirements.txt

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && gunicorn miempresa.wsgi --bind 0.0.0.0:8000"]


# Dockerfile
FROM python:3.11-slim

# 1) Instala librerías C necesarias para mysqlclient y Pillow
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev build-essential \
    libjpeg-dev zlib1g-dev \
  && rm -rf /var/lib/apt/lists/*

# 2) Copia el código al contenedor
WORKDIR /app
COPY . .

# 3) Instala pip (y ruedas) y tus dependencias Python
RUN pip install --upgrade pip setuptools wheel \
 && pip install -r requirements.txt

# 4) Expone el puerto 8000 (opcional, Railway lo detecta)
EXPOSE 8000

# 5) Al arrancar: migra y levanta Gunicorn
CMD ["sh", "-c", "python manage.py migrate && gunicorn miempresa.wsgi --bind 0.0.0.0:8000"]

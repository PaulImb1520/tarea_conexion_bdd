# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de la aplicación
COPY requirements.txt requirements.txt
COPY app.py app.py

# Instala las dependencias
RUN pip install -r requirements.txt

# Expone el puerto 5000
EXPOSE 5000

# Define el comando para ejecutar la aplicación
CMD ["python", "app.py"]
#Usa la imagen oficial de Python como base
FROM python:3
#Establece el directorio de trabajo en el contenedor
WORKDIR /usr/src/app

COPY requirements.txt ./
#Instala las dependencias del proyecto en el contenedor
RUN pip install --no-cache-dir -r requirements.txt
#Copia los archivos de tu proyecto en el contenedor
COPY . .
#EXPOSE PUERTO -> inciar mi puerto despues
#ejecuta tu archivo Python 
CMD [ "python", "app.py" ]

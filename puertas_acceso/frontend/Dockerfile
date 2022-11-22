#Contenedor que ejecuta una app muy simple de nfc para la lectura de los billetes, dado que la aquitectura es simple utilizamos la imagen alpine.

FROM python:3.8-alpine
RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh
RUN mkdir /app
WORKDIR /app
RUN pip install requests
COPY . .
CMD ["python", "puerta.py"]
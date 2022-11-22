# Dockerfile sobe el que se lanza el servicio de conexión con la api de la empresa de trenes, que utiliza JSON
FROM openjdk

COPY ./json.java /code/
WORKDIR /code
CMD ["java","json.java"]
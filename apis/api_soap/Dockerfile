# Dockerfile sobe el que se lanza el servicio de conexión con la api de la empresa 2, que utiliza SOAP
FROM openjdk

COPY ./soap.java /code/
WORKDIR /code
CMD ["java","soap.java"]
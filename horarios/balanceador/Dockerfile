#Contenedor donde se lanza un servicio de balanceo por si una replica front falla
FROM nginx

RUN rm /etc/nginx/conf.d/default.conf
COPY ./default.conf /etc/nginx/conf.d/
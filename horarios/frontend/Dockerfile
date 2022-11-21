FROM nginx

RUN mkdir public
COPY ./index.html /public/
RUN rm /etc/nginx/conf.d/default.conf
COPY ./default.conf /etc/nginx/conf.d/
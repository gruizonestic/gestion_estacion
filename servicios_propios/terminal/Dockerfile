# Terminal de fichaje, contenedor donde se lanza un nfc y en el que se transmiten los datos al backend.
FROM gcc:12.2.0
ADD ./main.c /code/
WORKDIR /code
RUN gcc main.c -o main
CMD ["./main"]
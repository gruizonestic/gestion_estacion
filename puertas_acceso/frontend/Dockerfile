    FROM gcc:latest
    RUN mkdir /PuertaDeAcceso
    COPY . /PuertaDeAcceso
    WORKDIR /PuertaDeAcceso/
    RUN gcc -o PuertaDeAcceso puerta.c
    CMD ["./PuertaDeAcceso"]
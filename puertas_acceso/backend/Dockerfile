# Contenedor donde se ejecuta el backend del servicio para acceder a la vías del tren, realiza peticiones a las diferenets 
#apis para poder verificar el billete con las diferentes empresas.

FROM golang
RUN mkdir /app
ADD . /app
WORKDIR /app
RUN go mod init feedme
RUN go mod tidy
RUN go build -o main .
RUN go env -w GO111MODULE=auto
EXPOSE 5207
CMD ["/app/main"]
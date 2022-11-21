FROM golang
RUN mkdir /app
ADD . /app
WORKDIR /app
RUN go mod init feedme
RUN go mod tidy
RUN go build -o main .
RUN go env -w GO111MODULE=auto
CMD ["/app/main"]
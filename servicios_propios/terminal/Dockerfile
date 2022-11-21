FROM ubuntu:22.04
ADD ./main.c /code/
WORKDIR /code
RUN apt update && apt install gcc -y
RUN gcc main.c -o main
CMD ["bash", "./main"]
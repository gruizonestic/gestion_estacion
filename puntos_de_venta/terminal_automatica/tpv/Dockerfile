FROM gcc:12.2.0
ADD ./main.c /code/
WORKDIR /code
RUN gcc main.c -o main
CMD ["./main"]
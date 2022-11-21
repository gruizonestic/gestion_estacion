FROM python:3.8-alpine
RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh
RUN mkdir /app
WORKDIR /app
RUN pip install requests
COPY . .
CMD ["python", "puerta.py"]
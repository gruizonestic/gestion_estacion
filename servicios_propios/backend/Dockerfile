#Servicio donde se ejecuta un temporizador que manda las señales a las api, así como inserta los datos de fichaje en la BBDD
FROM python:3.11
ADD ./main.py /code/
ADD ./requirements.txt /code/
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python3", "main.py"]
# Servicio donde se modifican los datos para poder ser transferidos al servicio central de gestion de puertas
FROM python:3.11
ADD ./main.py /code/
ADD ./requirements.txt /code/
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python3", "main.py"]
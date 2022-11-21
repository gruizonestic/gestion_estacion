FROM python:3.11
ADD ./main.py /code/
ADD ./requirements.txt /code/
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python3", "main.py"]
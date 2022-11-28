import requests
import random
import time
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

backend_url = 'http://puerta.backend:5207/validar'
billete = {'Numero': ''}

while True:
    numero_billete = random.randint(1, 99999)
    pasa_alguien = random.randint(1, 7)
    billete['Numero'] = str(numero_billete)
    time.sleep(pasa_alguien)

    try:
        x = requests.post(backend_url, json=billete, verify=False, timeout=10)
        print(x.text)
    except:
        x = requests.post(backend_url, json=billete, verify=False, timeout=10)

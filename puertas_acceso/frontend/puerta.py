import requests

url = 'http://puerta.backend1:5207/validar'
myobj = {'Numero' : '1234'}

x = requests.post(url, json = myobj)

print(x.text)
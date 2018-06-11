#!/usr/bin/python
# token SDfsdf567wer4554dsfdS8f943mer4wer87rZ6r4zdf4

import csv
import base64
import json
import requests
import random

with open('LOCALIDAD.csv') as f:
    d = dict(filter(None, csv.reader(f)))

idpoblacion = d.get("Albacete", "")
# Elige una poblacion aleatoriamente
idpoblacion = d.get(random.choice(list(d.keys())), "none")



api_url_base = 'http://www.aemet.es/es/apps/prediccion/municipios?req='
headers = {'Content-Type': 'application/json',
           'User-Agent': 'AEMET-AppClient-Android',
           'Accept': 'gzip'}

def get_repos(username):

    api_url = api_url_base + id
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return (response.content)
    else:
        print('[!] HTTP {0} calling [{1}]'.format(response.status_code, api_url))
        return None

# La aplicacion android de Aemet encripta las peticiones, cifrando el nombre de la poblacion ¿?
# Primero obtiene le codigo de la poblacion en la base de datos de la app , le añade un ; y un token
# Despues lo pasa a base64 y le hace un xor y lo vuelve a pasar a texto.

base64info = idpoblacion + ";SDfsdf567wer4554dsfdS8f943mer4wer87rZ6r4zdf4"
bArr = bytearray(base64info, 'ISO-8859-1')
base64info = "3e570pkt567wvg3r3e570pkt567wvg3r"
bArr2 = bytearray(base64info, 'ISO-8859-1')
bArr3 = bArr
for i in range(0,len(bArr)):

    bArr3[i] = bArr[i] ^ bArr2[i % len(bArr2)]
    #print (bArr3[i])

id = (base64.b64encode(bArr3)).decode("ISO-8859-1")

print (idpoblacion)

if idpoblacion != "" :
     print (get_repos(username))



# Usar la API de Have I been pwn?
import requests
import json
import logging
import getpass
#key = 'ec1e2ebed1754f1b8c00f2b90aa15906'
key = getpass.getpass(prompt="Ingrese su apikey: ")
headers = {}
headers['content-type']= 'application/json'
headers['api-version']= '3'
headers['User-Agent']='python'
#Place that API key here
headers['hibp-api-key']=key
try:
    #Preguntar correo a revisar
    email = input("Ingrese el correo a investigar: ")#'falso@hotmail.com'
    #solicitud
    url = 'https://haveibeenpwned.com/api/v3/breachedaccount/'+\
            email+'?truncateResponse=false'
    r = requests.get(url, headers=headers)       
    if r.status_code == 200:
        data = r.json()
        encontrados = len(data)
        if encontrados > 0:
            print("Los sitios en los que se ha filtrado el correo",email,"son:")
        else:
            print("El correo",email,"no ha sido filtrado")
        for filtracion in data:
            print(filtracion["Name"])
        msg = email+" Filtraciones encontradas: "+str(encontrados)
        print(msg)
        logging.basicConfig(filename='hibpINFO.log',
                            format="%(asctime)s %(message)s",
                            datefmt="%m/%d/%Y %I:%M:%S %p",
                            level=logging.INFO)
        logging.info(msg)
except requests.exceptions.RequestException as e:
    print(f"Ha habido un error con la solicitud: {e}")
    msg = r.text
    print(msg)
    logging.basicConfig(filename='hibpERROR.log',
                        format="%(asctime)s %(message)s",
                        datefmt="%m/%d/%Y %H:%M:%S",
                        level=logging.ERROR)
    logging.error(msg)
except requests.exceptions.ConnectionError as e:
    print(f"Ha habido un error en la conexión con al API: {e}") 
    msg = r.text
    print(msg)
    logging.basicConfig(filename='hibpERROR.log',
                        format="%(asctime)s %(message)s",
                        datefmt="%m/%d/%Y %H:%M:%S",
                        level=logging.ERROR)
    logging.error(msg)
except requests.exceptions.HTTPError as e:
    print(f"Ha habido un error http: {e}") 
    msg = r.text
    print(msg)
    logging.basicConfig(filename='hibpERROR.log',
                        format="%(asctime)s %(message)s",
                        datefmt="%m/%d/%Y %H:%M:%S",
                        level=logging.ERROR)
    logging.error(msg)
else:
    print(f"Ha habido un error inesperado") 
    msg = r.text
    print(msg)
    logging.basicConfig(filename='hibpERROR.log',
                        format="%(asctime)s %(message)s",
                        datefmt="%m/%d/%Y %H:%M:%S",
                        level=logging.ERROR)
finally:
    print("Ejecución finalizada")
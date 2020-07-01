#!/usr/bin/env python
import shodan
import configparser
import time
import sys

def anysearch():
    conteo = 1
    limite = 6 #HAY UN LIMITE DEFINIDO A 6 PARA MOSTRAR SÓLO 5 RESULTADOS, LO PUEDEN VARIAR

    print ("  " + "⌨️" * 70)
    print("""
    Elige una opción para realizar busquedas en Shodan:\n
    [+] Para buscar por SISTEMAS DE CONTROL INDUSTRIAL OPC digita [ 1 ].\n
    [+] Para realizar cualquier busqueda utilizando palabras claves digita [ 2 ].
    """)
    print ("  " + "⌨️" * 70 + "\n")
    selector = str(input("Escribe 1 o 2 según lo que quieras buscar: "))
    print("Tu selección fue el numero {}".format(selector))

    if selector == "1":
        #SHODAN_API_KEY2 = input("[!] \033[34mPor favor ingresa una API KEY válida para Shodan: \033[0m")
        api = shodan.Shodan(SHODAN_API_KEY2)
        time.sleep(0.5)
        busqueda = "port:4840"
        banner= "Información sobre SISTEMAS DE CONTROL INDUSTRIAL - OPC"
        print("\n\n")
    elif selector == "2":
        #SHODAN_API_KEY = input("[!] \033[34mPor favor ingresa una API KEY válida para Shodan: \033[0m")
        api = shodan.Shodan(SHODAN_API_KEY2)
        time.sleep(0.5)
        busqueda = input(menu_selec)
        banner= "Información general de tu búsqueda"
        print("\n\n")
    else:
        print("\nValor ingresado no es válido\n")
        exit()

    try:
        conteo = conteo + 1
        for inter in api.search_cursor(busqueda):
            print ("[+] \033[1;31mIP: \033[1;m" + (inter["ip_str"]))
            print ("[+] \033[1;31mPort: \033[1;m" + str(inter["port"]))
            print ("[+] \033[1;31mOrganización: \033[1;m" + str(inter["org"]))
            print ("[+] \033[1;31mLocalización: \033[1;m" + str(inter["location"]))
            print ("[+] \033[1;31mProtocolo: \033[1;m" + (inter["transport"]))
            print ("[+] \033[1;31mDominios: \033[1;m" + str(inter["domains"]))
            print ("[+] \033[1;31mHostnames: \033[1;m" + str(inter["hostnames"]))
            print ("[+] \033[1;31m",banner,"\033[1;m\n\n" + (inter["data"]))
            time.sleep(0.2)
            print ("\n[✅ ] Resultado: %s. de la búsqueda: %s" % (str(conteo), str(busqueda)))

            data = ("\nIP: " + inter["ip_str"]) + ("\nPort: " + str(inter["port"])) + ("\nOrganisation: " + str(inter["org"])) + ("\nLocation: " + str(inter["location"])) + ("\nLayer: " + inter["transport"]) + ("\nDomains: " + str(inter["domains"])) + ("\nHostnames: " + str(inter["hostnames"])) + ("\nData\n" + inter["data"])
            time.sleep(0.5)
            print ("\n" + "  " + "⌨️" * 70 + "\n")

            conteo += 1
            if conteo >= limite:
                exit()

    except shodan.APIError as e:
        print('Error: {} \033[1;31m[Tu API KEY ingresada no es válida]\033[0m'.format(e))

    except KeyboardInterrupt:
        print ("\n")
        print ("\033[1;55m[!] Proceso interrumpido por teclado! \033[0")
        time.sleep(0.3)
        print ("\n\n\t\033[1;55m[!] Vuelve cuando puedas \033[0m 🐱‍👤 \n\n")
        time.sleep(0.3)
        sys.exit(1)

header = ("""
\033[1;31m
      _                             _                      _             
 _   | |                    _      | |                _   (_)            
| |_ | | _   ____ ____ ____| |_    | | _  _   _ ____ | |_  _ ____   ____ 
|  _)| || \ / ___) _  ) _  |  _)   | || \| | | |  _ \|  _)| |  _ \ / _  |
| |__| | | | |  ( (/ ( ( | | |__   | | | | |_| | | | | |__| | | | ( ( | |
 \___)_| |_|_|   \____)_||_|\___)  |_| |_|\____|_| |_|\___)_|_| |_|\_|| |
                                                                  (_____|
By HY
\033[1;m
        \033[1;31m Shodan API \033[0m
        🐱‍👤 \t[Busqueda de objetivos]
""")

menu_selec = ("""[!] ¿Como hacer una busqueda efectiva en Shodan?
        ✔️ country: Para buscar en un país en específico.\033[1;31m country:py \033[0m
        ✔️ city: Filtro por ciudad.\033[1;31m city:”Los Angeles” \033[0m
        ✔️ port: Para buscar dispositivos que tengan un puerto abierto.\033[1;31m port:3306 \033[0m
        ✔️ net: Búsqueda de una ip específica o rangos de ip.\033[1;31m ip:182.93.44.0/24 \033[0m
        ✔️ hostname: Busca el texto que le indiquemos en el nombre del host.\033[1;31m hostname:iplocal \033[0m
        ✔️ geo: Buscar dispositivos mediante coordenadas.\033[1;31m geo:32.9775,-70.1293 \033[0m
        ✔️ os: Para listar un sistema operativo determinado.\033[1;31m os:Linux \033[0m
        ✔️ after: Dispositivos agregados después de la fecha.
        ✔️ before: Lo mismo, pero antes de la fecha.\033[1;31m after/before:27/03/2015 \033[0m
        ✔️ has_screenshot:true Nos muestra dispositivos de los cuales hay una captura.\n
         [+] A continuación ingresa tu búsqueda: """)


config = configparser.ConfigParser()
config.read('config.ini')
SHODAN_API_KEY2 = config['DEFAULT']['SHODAN_API_KEY']


if __name__ == '__main__':
    print(header)
    anysearch()

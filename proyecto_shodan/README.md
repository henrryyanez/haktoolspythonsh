## IOC_SHODAN

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://desplieguedigital.com)

##### Esta tool busca poder consultar de manera interactiva indicadores de compromiso en shodan.

Requerimientos para consultar:
- Ingresar los valores de SHODAN_API_KEY dentro del archivo config.ini.

`- Colocar en la misma ruta el archivo target.txt con los IOC a consultar:`

```sh
$ python3 shodan_ioc.py
```

La consulta arroja una ventana interactiva de consultas:


Salida:
```
      _                             _                      _             
 _   | |                    _      | |                _   (_)            
| |_ | | _   ____ ____ ____| |_    | | _  _   _ ____ | |_  _ ____   ____ 
|  _)| || \ / ___) _  ) _  |  _)   | || \| | | |  _ \|  _)| |  _ \ / _  |
| |__| | | | |  ( (/ ( ( | | |__   | | | | |_| | | | | |__| | | | ( ( | |
 \___)_| |_|_|   \____)_||_|\___)  |_| |_|\____|_| |_|\___)_|_| |_|\_|| |
                                                                  (_____|
By HY

         Shodan API 
        🐱‍👤  [Busqueda de objetivos]

  ⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️⌨️

    Elige una opción para realizar busquedas en Shodan:

    [+] Para buscar por SISTEMAS DE CONTROL INDUSTRIAL OPC digita [ 1 ].

    [+] Para realizar cualquier busqueda utilizando palabras claves digita [ 2 ].
```

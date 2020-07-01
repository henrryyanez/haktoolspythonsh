## haktoolspython
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://desplieguedigital.com)

##### Esta tool busca poder consultar de manera masiva indicadores de compromiso en varias fuentes, X-Force (IBM), Whois, Virustotal, Shodan.

Requerimientos para consultar:
- Ingresar los valores de API_KEY y API_PASSWORD dentro del archivo config.ini.
- El archivo target.txt debe contener las URL o IP para que el programa lo consulte.

`- Colocar en la misma ruta el archivo target.txt con los IOC a consultar:`

```sh
$ python3 ioc_reputation_hy.py
```

La consulta arroja el perfil de riesgo relacionado al IOC ingresado:

Campos resutantes:
ip,score_risk, risk_category, fecha_whois, fecha_update, country_whois

Salida:
```
190.12.8.162,1,{'Dynamic IPs': 71},2003-02-21T00:00:00.000Z,2019-10-07T00:00:00.000Z,roberto@PUNTO.NET.EC
google.com,1,{'Search Engines / Web Catalogues / Portals': True},1997-09-15T07:00:00.000Z,2019-09-09T15:39:04.000Z,abusecomplaints@markmonitor.com
```

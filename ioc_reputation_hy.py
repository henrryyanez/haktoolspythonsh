#!/usr/bin/env python
'''
[HY]
---------------------------
Autor: Henrry Yanez
Version: 1.2
Descripcion:
Programa creado para consumir un archivo de IP/URL y consultar reputación XForce de manera masiva.
Crear archivo con los datos llamado:  target.txt y ubicar tu pripia API KEY de XForce
'''

__author__ = "Henrry Yanez"
__version__ = "1.3"

import requests, base64
import socket
import configparser
import json
import re
import time
import sys
# ================================================================
#   TRABAJANDO CON LA API DE XFORCE --- REVISIÓN MASIVA DE IOC'S
#   REALIZADO POR HENRRY YANEZ
# ================================================================


def read_lines():
    with open('target.txt','r') as fi:
        lines = fi.readlines()

        for line in lines:
            if re.match('[0-9]+(?:\.[0-9]+){3}', line.strip()) is None:
                line = line.strip()
                requesturl(line)
            else:
                line = line.strip()
                requestip(line)


def requesturl(url):
    info_url = ibm.get_url_info(url_mode='report', url=url)
    response_whois = ibm.get_whois_info(entity=url)

    fecha_whois = response_whois['createdDate']
    fecha_update = response_whois['updatedDate']
    country_whois = response_whois.get('contactEmail')
    # registrante_whois = response_whois['registrarName']
    score_url = info_url['result']['score']
    cats_url = info_url['result']['cats']

    out_url = (url,score_url, cats_url, fecha_whois, fecha_update, country_whois)
    print("{},{},{},{},{},{}".format(url,score_url, cats_url, fecha_whois, fecha_update, country_whois))

    fo = open('reporte.txt', 'a')
    fo.write(str(out_url))
    fo.write("\n")
    fo.flush()
    fo.close()



def requestip(ip):
    info_ip = ibm.get_ip_info(ip_mode='report', ip=ip)

    response_whois = ibm.get_whois_info(entity=ip)
    fecha_whois = response_whois['createdDate']
    fecha_update = response_whois['updatedDate']
    country_whois = response_whois.get('contactEmail')
    #registrante_whois = response_whois['registrarName']
    #score_info = info_ip['score']
    score_info = info_ip.get("score")

    #cats_info = info_ip['cats']
    cats_info = info_ip.get('cats')
    out_ip = (ip,score_info, cats_info, fecha_whois, fecha_update, country_whois)
    print("{},{},{},{},{},{}".format(ip, score_info, cats_info, fecha_whois, fecha_update, country_whois))

    fo = open('reporte.txt', 'a')
    fo.write(str(out_ip))
    fo.write("\n")
    fo.flush()
    fo.close()


class IBMXForce:

    # ----------------------------------------------------------------------------
    #   CONSTRUCTOR DE REPORTES DE IOC'S
    # ----------------------------------------------------------------------------
    def __init__(self, api_key, api_password):
        self._headers = {'Authorization': self.convert_to_base64(api_key=api_key, api_password=api_password)}
        # API RELACIONADA A IP ADDRESS
        self._ip_report_api = "https://api.xforce.ibmcloud.com/ipr/{ip}"
        # API RELACIONADA A URL/DOMAIN
        self._url_report_api = "https://api.xforce.ibmcloud.com/url/{url}"
        # API RELACIONADA A WHOIS
        self._whois_api = "https://api.xforce.ibmcloud.com/whois/{host}"
    # --------------------------------------------------------------------------------
    #   CONVIRTIENDO LA API KEY Y LA API PASSWORD A FORMATO BASE64 ENCODED PARA LA AUTENTICACION
    # --------------------------------------------------------------------------------
    def convert_to_base64(self, api_key, api_password):
        # convirtiendo el str a bytes
        string_format = f'{api_key}:{api_password}'.encode()
        # convirtiendo bytes al formato base64 encode y normalizando a string
        base64_format = f'Basic {base64.b64encode(string_format).decode()}'
        return base64_format

    # -------------------------------------------------------------------------
    #   PROVIDE IP ADDRESS TO GET INFORMATION RELATED TO RESPSECTIVE API CALL
    # -------------------------------------------------------------------------
    def get_ip_info(self, ip_mode, ip):
        response = None
        if ip_mode == 'report': response = requests.get(url=self._ip_report_api.replace("{ip}", ip), headers=self._headers)
        if response is not None:
            if response.status_code == 200:
                return response.json()  # returns json but parse data with customized information
            # If HTTP status code is not 200 then it will print status code and the reason behind it
            else:
                print(f'Status Code : {response.status_code} | Reason : {response.reason}')
                return None
        else: return None

    # -------------------------------------------------------------------------
    #   PROVIDE URL OR DOMAIN TO GET INFORMATION RELATED TO RESPSECTIVE API CALL
    # -------------------------------------------------------------------------
    def get_url_info(self, url_mode, url):
        response = None
        # make a request to ibm using respective api call
        if url_mode == 'report': response = requests.get(url=self._url_report_api.replace("{url}", url), headers=self._headers)
        if response is not None:
            if response.status_code == 200:
                return response.json()  # returns json but parse data with customized information
            # If HTTP status code is not 200 then it will print status code and the reason behind it
            else:
               print(f'Status Code : {response.status_code} | Reason : {response.reason}')
               return None
        else: return None


    # -----------------------------------------------------------------------------------------
    #   PROVIDE IP ADDRESS (OR) URL (OR) DOMAIN TO GET INFORMATION FROM WHOIS
    # -----------------------------------------------------------------------------------------
    def get_whois_info(self, entity):
        # make a request to ibm using respective api call
        response = requests.get(url=self._whois_api.replace("{host}", entity), headers=self._headers)
        if response.status_code == 200:
            return response.json()  # returns json but parse data with customized information
        # If HTTP status code is not 200 then it will print status code and the reason behind it
        else:
            print(f'Status Code : {response.status_code} | Reason : {response.reason}')
            return None

# ----------------------------------------------
#   INVOKE METHODS
# ----------------------------------------------

XFORCE_API_KEY2=""
XFORCE_API_PASS2=""
config = configparser.ConfigParser()
config.read('config.ini')
XFORCE_API_KEY2 = config['DEFAULT']['XFORCE_API_KEY']
XFORCE_API_PASS2 = config['DEFAULT']['XFORCE_API_PASS']


ibm = IBMXForce(api_key=XFORCE_API_KEY2, api_password=XFORCE_API_PASS2) 


if __name__ == '__main__':
    read_lines()

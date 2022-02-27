# Codigo buscar dados OLX
#by Francisco S Burigo

import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import json
from difflib import SequenceMatcher
from selenium import webdriver
import time
from datetime import date
import re
from selenium.webdriver.chrome.options import Options


ListaURLS = []
listaJson =[]
Dictdt= []
Dictdd= []

#busca URLS dos anuncios e salva em uma lista
def buscaURLsOLX(pages = 3):
    #https://sc.olx.com.br/florianopolis-e-regiao/imoveis/terrenos/compra
    
    
    for x in range(1, pages):
        
        url = "https://sc.olx.com.br/florianopolis-e-regiao/imoveis/terrenos/compra?o=" + str(x)
        

        

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}


        page = requests.get(url = url, headers=headers)
        soup = BeautifulSoup(page.content,'lxml')
        itens = soup.find_all("li", {"class" : "sc-1fcmfeb-2 fvbmlV"})
        

        for a in itens :
            try:
                URL_anuncio = a.find("a")["href"]
                
                ListaURLS.append(URL_anuncio)
                
            except:
                print("erro")
            

            

        

    return(ListaURLS)


def buscaDadosOLX(ListaURLS):
    N_Pag = len(ListaURLS)

    for x in range(0, 2):
        
        #url = "https://sc.olx.com.br/florianopolis-e-regiao/terrenos/terreno-990m-de-esquina-996439294"
        url = ListaURLS[x]
        
            
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}
        

        #chrome_options = Options()
        # maximized window
        #chrome_options.add_argument("--start-maximized")
        
        #page = requests.get(url = url, headers=headers)
        browser = webdriver.Chrome()
        browser.get(url)
        
        browser.maximize_window()
        
        time.sleep(5)
        html = browser.page_source
        #soup = BeautifulSoup(page.content,'lxml')
        soup = BeautifulSoup(html,'lxml')
        #print(soup)
        
        Titulo = soup.find("h1",{"class" : "sc-45jt43-0 eCghYu sc-ifAKCX cmFKIN"}).get_text()
        Preco = soup.find("h2",{"class" : "sc-1wimjbb-2 iUSogS sc-ifAKCX cmFKIN"}).get_text()
        Preco = Preco.split("R$")[1]
        Preco = float(Preco.replace(".",""))
        Descricao = soup.find("span",{"class" : "sc-1sj3nln-1 eOSweo sc-ifAKCX cmFKIN"}).get_text()
        NomeVendedorURL = soup.find("span",{"class": "sc-fBuWsC sc-cnTzU hWZqZT sc-hARARD enkigN sc-ifAKCX kanYPz"}).get_text()
        ddclass = soup.find_all("dd",{"class": "sc-1f2ug0x-1 ljYeKO sc-ifAKCX kaNiaQ"})
        dtclass = soup.find_all("dt",{"class": "sc-1f2ug0x-0 cLGFbW sc-ifAKCX cmFKIN"})
        #teste = soup.find("script", {"id" : "initial-data"})
        #print(teste)
        #data = json.loads(teste.get_text())
        print(NomeVendedorURL)
##
##        for a in NomeVendedorURL:
##            try:
##                URL_vendedor = a.find("a")["href"]
##
##                print(URL_vendedor)
##                
##                
##            except:
##                print("erro")
##    
        

       
        for a in range(0, len(ddclass)):
            Dictdt.append(dtclass[a+ 1].get_text())
            Dictdd.append(ddclass[a].get_text())

        dict_tamanho_localizacao = dict(zip(Dictdt, Dictdd))

        json = {"Titulo" : Titulo,
                "Preco" : Preco,
                "NomeVendedor" : NomeVendedorURL,
                "Descricao" : Descricao,
                

            }
        json.update(dict_tamanho_localizacao)

        

        
        listaJson.append(json)


        

        browser.close()
        
        

        
        
            
            
        

buscaURLsOLX()
buscaDadosOLX(ListaURLS)
df = pd.DataFrame(listaJson)
df.to_csv("Terrenos.csv")


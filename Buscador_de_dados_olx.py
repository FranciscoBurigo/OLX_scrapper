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

ListaURLS = []

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

    for x in range(0, 6):
        
        #url = "https://sc.olx.com.br/florianopolis-e-regiao/terrenos/terreno-990m-de-esquina-996439294"
        url = ListaURLS[x]
        

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}


        page = requests.get(url = url, headers=headers)
        soup = BeautifulSoup(page.content,'lxml')
        Titulo = soup.find("h1",{"class" : "sc-45jt43-0 eCghYu sc-ifAKCX cmFKIN"}).get_text()
        Preco = soup.find("h2",{"class" : "sc-1wimjbb-2 iUSogS sc-ifAKCX cmFKIN"}).get_text()
        Descricao = soup.find("span",{"class" : "sc-1sj3nln-1 eOSweo sc-ifAKCX cmFKIN"}).get_text()
        NomeVendedor = soup.find("div",{"id": "miniprofile"},{"class": "sc-fBuWsC sc-jGFFOr iNEwhQ sc-hARARD ksmUnv sc-ifAKCX cmFKIN"}).get_text()
        ddclass = soup.find_all("dd",{"class": "sc-1f2ug0x-1 ljYeKO sc-ifAKCX kaNiaQ"})
        dtclass = soup.find_all("dt",{"class": "sc-1f2ug0x-0 cLGFbW sc-ifAKCX cmFKIN"})
        teste = soup.find_all("script")
        print(teste[7].get_text())

       
        #for a in range(0, len(ddclass)):
            #print(dtclass[a+1].get_text()  + ":" + ddclass[a].get_text())


        print(NomeVendedor)
        print(Titulo)
        print(Preco)
        print(Descricao)
        
        
        

        
        
            
            
        

buscaURLsOLX()
buscaDadosOLX(ListaURLS)

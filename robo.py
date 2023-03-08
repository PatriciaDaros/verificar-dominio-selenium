from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import xlrd
import pandas as pd
import openpyxl
import numpy

dominios = []

arquivo = open('dominio.txt', 'r')
arq = open("resultado.txt","w")

for linha in arquivo:
	linha = linha.strip()
	dominios.append(linha)

driver = webdriver.Chrome()
driver.get("https://registro.br/")
time.sleep(10)

for dominio in dominios:
    pesquisa = driver.find_element("id","is-avail-field")
    pesquisa.clear() #Limpando a barra de pesquisa
    pesquisa.send_keys(dominio)
    pesquisa.send_keys(Keys.RETURN)
    
    strong = driver.find_elements(By.TAG_NAME, "strong")

    texto = ("Dominio %s %s\n" % (dominio, strong[4].text))
    arq.write(texto)

    time.sleep(5)

arq.close()
arquivo.close()
driver.close()
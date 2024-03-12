from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait

import time
import os

chaves = []
caminho_arquivo = open(os.path.join("C:/Users/romar/Downloads/chaves_teste/nf_sao_judas_sp.txt"), 'r')

#------------------ extrair e armazenar as chaves do arquivo .txt no array -------------------------

conteudo = caminho_arquivo.read()

for chave in conteudo.split():
    chaves.append(chave)

caminho_arquivo.close()

#--------- instala versão atual do webdriver do navegador(no caso, chrome)----------------

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service = servico)

#--------- acessa o site especificado e vai até a tela especificada ----------------

navegador.get("https://nfe.fazenda.sp.gov.br/ConsultaNFe/consulta/publica/ConsultarNFe.aspx")

botaoOcultarDetalhes = navegador.find_element('xpath', '//*[@id="details-button"]')
botaoOcultarDetalhes.click()

time.sleep(5)

irParaSefaz = navegador.find_element('xpath', '//*[@id="proceed-link"]')
irParaSefaz.click()

time.sleep(5)

#------------------ loop para pegar um chave por vez -------------------------

total = 0
while total < len(chaves):
    chave = (chaves[total])

    inserirChaveNoCampo = navegador.find_element('xpath', '//*[@id="ContentMain_tbxIdNFe"]')
    inserirChaveNoCampo.send_keys(chave)

    time.sleep(5)
    
    botaoCaptcha = navegador.find_element('xpath', '//*[@id="recaptcha-anchor"]/div[1]')
    botaoCaptcha.click()

    time.sleep(5)

    botaoDownload = navegador.find_element('xpath', '//*[@id="ContentMain_btnConsultaResumida"]')
    botaoDownload.click()
    
    total += 1



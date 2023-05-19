"""
O que vamos aprender:
Na terceira aula da Semana do Python, você vai aprender a criar um código para automação de processos. No dia a dia das
empresas, é muito comum que existam operações manuais que além de extremamente repetitivas (chatas) são suscetíveis a
erro visto que são feitas de forma manual. Vamos aprender como criar um código com o qual você possa resolver esse problema
sem nem tocar no mouse ☺. Aprenda como fazer uma automação com integração web com os conceitos abaixo:
"""

# Importando bases | de dados do Excel | Importando bibliotecas | Webdriver Usando Selenium #

from selenium import webdriver
import pandas as pd
import unicodedata

navegador = webdriver.Chrome()
navegador.get("https://www.google.com/")

tabela = pd.read_excel("Aula 3/commodities.xlsx")
print(tabela)


for linha in tabela.index:
    produto = tabela.loc[linha, "Produto"]
    
    print(produto)
    produto = produto.replace("ó", "o").replace("ã", "a").replace("á", "a").replace(
    "ç", "c").replace("ú", "u").replace("é", "e")
    
    link = f"https://www.melhorcambio.com/{produto}-hoje"
    print(link)
    navegador.get(link)

    preco = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
    preco = preco.replace(".", "").replace(",", ".")
    print(preco)
    tabela.loc[linha, "Preço Atual"] = float(preco)


print("Acabou")
print(tabela)
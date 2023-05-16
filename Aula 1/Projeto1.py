# Automação de tarefas e organização de dados

# Desafio:

# Para controle de custos, todos os dias, seu chefe pede um relatório com todas as compras de mercadorias da empresa.
# O seu trabalho, como analista, é enviar um e-mail para ele, assim que começar a trabalhar, com o total gasto, a 
# quantidade de produtos compradas e o preço médio dos produtos.
# E-mail do seu chefe: para o nosso exercício, coloque um e-mail seu como sendo o e-mail do seu chefe<br>
# Link de acesso ao sistema da empresa: https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema

# para resolver isso, vamos usar o pyautogui, uma biblioteca de automação de comandos do mouse e do teclado

import pandas as pd
import pyautogui, time, pyperclip

# entrando no sistema

time.sleep(2)
pyautogui.hotkey("win")
pyautogui.write("Chrome")
time.sleep(2)
pyautogui.hotkey("enter")


time.sleep(1)
pyautogui.write("https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")

time.sleep(1)
pyautogui.press("enter")

# fazendo login
time.sleep(1)
pyautogui.click(796,380)
pyautogui.write("usuário")
pyautogui.hotkey("tab")
pyautogui.write("senha123")
pyautogui.hotkey("tab")
pyautogui.hotkey("enter")


# baixando dados
time.sleep(3)
pyautogui.click(492,358)

time.sleep(3)
pyautogui.click(534,777)


# Calculando os indicadores

tabela = pd.read_csv(r"C:\Users\Wellington\Downloads\Compras.csv", sep=";")

print(tabela)
total_gasto = tabela["ValorFinal"].sum()
quantidade = tabela["Quantidade"].sum()
preco_medio = total_gasto / quantidade
print(f"R$ {total_gasto:.2f}")
print(f"R$ {quantidade:.2f}")
print(f"R$ {preco_medio:.2f}")

# entrar no email: https://mail.google.com/mail/u/0/#inbox
time.sleep(3)
pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://mail.google.com/mail/u/0/#inbox")
pyautogui.press("enter")




time.sleep(2)
pyautogui.click(95, 204)

time.sleep(2)
pyautogui.write("pythonimpressionador@gmail.com")
time.sleep(2)
pyautogui.hotkey("enter")
time.sleep(2)
pyautogui.hotkey("tab")

time.sleep(2)
pyperclip.copy("Relatório de Vendas")
pyautogui.hotkey("ctrl", "v")
time.sleep(2)

pyautogui.press("tab")


texto = f"""
Prezados,
Segue o relatório de compras

Total Gasto: R${total_gasto:,.2f}
Quantidade de Produtos: {quantidade:,}
Preço Médio: R${preco_medio:,.2f}

Qualquer dúvida, é só falar.
Att., Wellington Almeida
"""

pyperclip.copy(texto)

pyautogui.hotkey("ctrl", "v")
time.sleep(2)

# enviar
pyautogui.hotkey("ctrl", "enter") 
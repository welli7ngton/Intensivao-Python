# importando biblioteca para manuseio dos dados
import pandas as pd 

# criando tabela
tabela = pd.read_csv("Aula 2/clientes.csv", encoding="latin1", sep=";")

# removendo dados inúteis da tabela
'''
Para retirarmos a coluna Unnamed: 8, vamos usar o método .drop()

Este método será aplicado na variável tabela criada na primeira linha do
código para receber os dados do arquivo .csv. Este método vai precisar de
alguns argumentos:
    • Nome da coluna ou código da linha a ser removida: ('Unnamed: 8')
    • Qual dos eixos deve ser excluído:
    • 0 ou 'index' será apagada a linha indicada;
    • 1 ou 'columns' será apagada a coluna indicada.
'''

tabela = tabela.drop("Unnamed: 8", axis=1)

print(tabela)

# Tratamento e visão geral dos dados

tabela["Salário Anual (R$)"] = pd.to_numeric(tabela["Salário Anual (R$)"], errors="coerce")
'''
o atributo coerce → Indica que em caso de erro, o valor a ser
considerado na transformação será NaN (Not a Number,
não é um número).
'''

tabela = tabela.dropna()
print(tabela.info())



# Analisando os dados

print(tabela.describe())


import plotly.express as px

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, y="Nota (1-100)", text_auto=True, histfunc="avg", nbins=10)
    grafico.show()
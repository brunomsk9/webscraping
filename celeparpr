import requests
from bs4 import BeautifulSoup
import re
from pandasql import sqldf
import pandas as pd

link = "https://celepar7.pr.gov.br/ceasa/hoje.asp"


requisicao = requests.get(link)

site = BeautifulSoup(requisicao.text, "html.parser")

# localiza as linhas das tabelas
list_produtos = [i.get_text() for i in site.find_all('tr')]

# quebra em colunas
dados_linhas = [linha.split('\n') for linha in list_produtos]

# converte lista em dataframe
df = pd.DataFrame(dados_linhas[1:],columns=['Data','Produto','Curitiba','Maringá','Londrina','Foz do Iguaçu','7','Cascavel'])

# elimina as linhas nulos
#df.dropna(inplace=True)

# recorte final de colunas
colunas = ['Data','Produto','Curitiba','Maringá','Londrina','Foz do Iguaçu','Cascavel']

# 
df = df[colunas]
df_final = df.drop([0,1])

#Inserir Data de Atualização
df_data = pd.to_datetime(pd.Series([pd.Timestamp.now(), None])) 
t = pd.DataFrame(df_data[0:],columns=['Data'])
df_data_final = t.drop([1])
df_data_final = df_data_final.astype(str)

tabela = pd.merge(df_final,df_data_final,how='outer') 

print(tabela)

tabela.to_csv("C:/mnt/arquivo.csv",index=False)
tabela.to_excel("C:/mnt/arquivo.xlsx",index=False)


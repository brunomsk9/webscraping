import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

#link = "https://www.agrolink.com.br/cotacoes/ceasa/hortalicas/abobora/abobora-1kg/"
link = "https://www.agrolink.com.br/cotacoes/ceasa/busca/"

requisicao = requests.get(link)

site = BeautifulSoup(requisicao.text, "html.parser")

# localiza as linhas das tabelas
list_produtos = [i.get_text() for i in site.find_all('tr')]

# quebra em colunas
dados_linhas = [linha.split('\n') for linha in list_produtos]

# converte lista em dataframe
df = pd.DataFrame(dados_linhas[1:],columns=['1','2','Produto','4','5','Ceasa','localidade','valor','data','10'])

# elimina as linhas nulos
df.dropna(inplace=True)

# recorte final de colunas
colunas = ['Produto', 'Ceasa', 'localidade', 'valor', 'data']
df = df[colunas]

print(df)

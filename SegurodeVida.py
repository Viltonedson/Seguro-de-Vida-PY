import pandas as pd
import matplotlib.pyplot as plt

# Ler os dados do arquivo CSV\n\n
dados = pd.read_csv('seguro_de_vida.csv')
print("\n")

# Exibir as primeiras linhas dos dados
print(dados.head())
print("\n")

#Exibir informaçoes do DataFrame
print(dados.info())
print("\n")

#Exibir Valores que faltam \n
print(dados.isnull().sum())
print("\n")

#Exibir estatisticas descritivas
print(dados.describe())
print("\n")

#Exibir medidas descritivas das variáveis categóricas
print(dados.describe(include=['object']))
print("\n")

#Número de filhos mais frequente
print(dados['filhos'].mode(0))
print("\n")

#Clientes fumantes
percentual_fumantes = (dados['fumante'].value_counts(normalize=True) * 100)['sim']
print(f"{percentual_fumantes:.2f}%")
print("\n")


#Quantidade de categorias na variáve da região
print(dados['regiao'].value_counts())
print("\n")
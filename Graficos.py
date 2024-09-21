import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")


# Criando o gráfico de barras
regioes = dados['regiao'].value_counts()
cores = ['red', 'cyan', 'green', 'purple']
plt.figure(figsize=(12, 8))
regioes.plot(kind='bar', edgecolor='black', color=cores)
plt.title('Número de Clientes por Região')
plt.xlabel('REGIÃO')
plt.ylabel('NÚMERO DE CLIENTES')
plt.savefig('regiao.png', bbox_inches='tight')
plt.show()

print("\n")

fumantes = dados['fumante'].value_counts()

# Criando o gráfico de pizza
plt.figure(figsize=(8, 8))
fumantes.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['green', 'orange'])
plt.axis('equal')
plt.title('Proporção de Clientes Fumantes')
plt.ylabel('')
plt.savefig('clientesFumantes.png', bbox_inches='tight')
plt.show()

print("\n")

#Criando Histograma
plt.figure(figsize=(12, 8))
dados['idade'].plot(kind='hist', bins=20, edgecolor="black")
sns.histplot(dados['idade'], bins=20, kde=False, palette='viridis')
plt.grid(True, linestyle='--', alpha=0.7)
plt.title('Distribuição das Idades dos Clientes', fontsize=15)
plt.xlabel('Idade', fontsize=12)
plt.ylabel('Frequência', fontsize=12)
plt.savefig('idadeClientes.png', bbox_inches='tight')
plt.show()
print("\n")

#Gráfico de Dispersao
plt.figure(figsize=(12, 8))
plt.scatter(dados['idade'], dados['despesas'], c=dados['idade'], cmap='viridis', alpha=0.7, s=100, edgecolors='white', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.7)
cbar = plt.colorbar()
cbar.set_label('Idade')
plt.title('Relação entre Idade e Salário', fontsize=15)
plt.xlabel('Idade', fontsize=12)
plt.ylabel('Salário', fontsize=12)
plt.savefig('despesas.png', bbox_inches='tight')
plt.show()


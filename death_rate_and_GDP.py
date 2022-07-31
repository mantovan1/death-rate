import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('world.csv')

perCapita = dados['GDP - per capita']
taxaMorte = dados['Death rate(deaths/1000 population)']

plt.xlabel('Renda Per Capita')
plt.ylabel('Taxa de Morte')
plt.scatter(perCapita, taxaMorte)
plt.show()

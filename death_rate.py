import pandas as pd
import matplotlib.pyplot as plt

world = pd.read_csv('world.csv')
world.hist(column='Death rate(deaths/1000 population)', bins=100)

plt.show()
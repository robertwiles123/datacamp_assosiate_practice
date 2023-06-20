# create visual better
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Reading file to dataframe
coffee = pd.read_csv('coffee_clean.csv')

# make graph prettier
# add labeled title etc.
sns.lineplot(x='Rating', y='Reviews', data=coffee)
plt.minorticks_on()
plt.grid(which='both', linewidth=0.5, alpha=0.5, linestyle='--')
plt.savefig('question4_visual.png', format='png')
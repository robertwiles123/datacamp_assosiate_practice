# create visual better
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Reading file to dataframe
coffee = pd.read_csv('coffee_clean.csv')

#to drop the annomaly
coffee_cleaned = coffee.loc[coffee['Reviews'] != 17937.0]


# make graph prettier
# add labeled title etc.
sns.boxplot(x='Rating', y='Reviews', data=coffee_cleaned)
plt.savefig('question4_visual.png', format='png')
# comment code
# create visual better
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Reading file to dataframe
coffee = pd.read_csv('coffee.csv')

print(coffee.columns)

stores_grouped_rating = coffee.groupby('Rating')['Place name'].count()

print(stores_grouped_rating)

sns.lineplot(x=stores_grouped_rating.index, y=stores_grouped_rating.values)
plt.xlabel('Ratings')
plt.ylabel('Number of resturants')
plt.ylim(0,50)
plt.grid()
plt.savefig('question2_visual.png', format='png')


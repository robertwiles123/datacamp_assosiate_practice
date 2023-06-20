# create visual better
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Reading file to dataframe
coffee = pd.read_csv('coffee_clean.csv')

# to count how many stores go each potential rating
stores_grouped_rating = coffee.groupby('Rating')['Place name'].count()

# To see as a table
print(stores_grouped_rating)

# create and save a graph
sns.lineplot(data=stores_grouped_rating, markers=True)
plt.savefig('question2_visual.png', format='png')


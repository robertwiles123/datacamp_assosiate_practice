# create visual better
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Reading file to dataframe
coffee = pd.read_csv('coffee_clean.csv')

# to count how many stores go each potential rating
stores_grouped_rating = coffee.value_counts('Rating')

print(stores_grouped_rating)

sns.set_palette("colorblind")
sns.histplot(stores_grouped_rating.index, kde=True)
plt.title('Distribution of resturant ratings', y=1.1)
plt.xlabel('Ratings')
plt.savefig('question3_visual.png', format='png')
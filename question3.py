# create visual better
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Reading file to dataframe
coffee = pd.read_csv('coffee_clean.csv')

# To count number of reviews
stores_grouped_rating = coffee.value_counts('Reviews')

print(stores_grouped_rating)

sns.set_palette("colorblind")
sns.histplot(stores_grouped_rating.index, kde=True)
plt.title('Distribution for number of resturant reviews')
plt.xlabel('Reviews')
plt.savefig('question3_visual.png', format='png')

plt.clf()

stores_grouped_rating_clean = stores_grouped_rating.drop(17937.0)

sns.set_palette('colorblind')
sns.histplot(stores_grouped_rating_clean.index, kde=True)
plt.title('Distribution for number of resturant reviews', y=1.05)
plt.xlabel('Reviews')
plt.savefig('question3_visual_clean.png', format='png')

stores_grouped_rating_clean.to_csv('coffee_clean_v2.csv')
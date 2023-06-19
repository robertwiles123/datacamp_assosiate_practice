import pandas as pd
import numpy as np

# Reading file to dataframe
coffee = pd.read_csv('coffee.csv')

# checking import successfull
print(coffee.head())

# get basic information about dataframe
print(coffee.info())

# To get every unique value for the dataframe. Quick to write, but made it hard to read
# Unique_values = {col: coffee[col].unique() for col in coffee.columns}

# print(unique_values)

# Median review score to fill the reviews
median_review = np.nanmedian(coffee['Reviews'])

print(median_review)

# Dict of columns to change NaN and what they should change to
cols_to_clean = {'Rating': 0,
                 'Reviews':  median_review,
                 'Dine in option': False,
                 'Takeout option': False}

# Fill the nan with the correct values
coffee_clean = coffee.fillna(cols_to_clean)


print(coffee_clean.info())
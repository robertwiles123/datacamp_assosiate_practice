import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

#read in coffee csv
coffee = pd.read_csv('coffee_clean_v3.csv')

# Boolean columns that need to be converted using Label encoder
boolean_columns = ['Delivery option', 'Dine in option', 'Takeout option']

label_encoder = LabelEncoder()
for column in boolean_columns:
    coffee[column] = label_encoder.fit_transform(coffee[column])

# Collumns that are objects so need one hot encoding
object_columns = ['Region', 'Place name', 'Place type', 'Price']

# Perform one-hot encoding
coffee_encoded = pd.get_dummies(coffee, columns=object_columns)

# Assign dependent and independent models
y = coffee_encoded['Reviews']
X = coffee_encoded.drop('Reviews', axis=1)

#split them in to 80/20 train test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=27)

# Starting model
linear = LinearRegression()

# Fitting data
linear.fit(X_train, y_train)

# Creating a prediction
y_pred = linear.predict(X_test)

# Getting the MSE
mse = mean_squared_error(y_test, y_pred)

# Calculate mean absolute error (MAE)
mae = mean_absolute_error(y_test, y_pred)

# Calculate R-squared (coefficient of determination)
r2 = r2_score(y_test, y_pred)

# Print the evaluation metrics
print("Mean Squared Error (MSE):", mse)
print("Mean Absolute Error (MAE):", mae)
print("R-squared (R2):", r2)
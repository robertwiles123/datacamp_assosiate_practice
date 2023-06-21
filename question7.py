import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
# Only needed if updating the Grid Search
# from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score

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
"""
# To find the best peramators for the model
param_grid = {
    'max_depth': [3, 5, 7, 10],
    'n_estimators': [50, 100, 200],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'max_features': ['sqrt', 'log2'],
    'max_samples': [None, 0.5, 0.8],
    'bootstrap': [True, False],
    'random_state': [42]
}

# Starting model
rf_model = RandomForestRegressor()

# Perform grid search with cross-validation
grid_search = GridSearchCV(rf_model, param_grid, cv=5, scoring='neg_mean_squared_error')
grid_search.fit(X_train, y_train)

# Print the best hyperparameters and corresponding score
print("Best hyperparameters:")
print(grid_search.best_params_)
print("Best Score (Negative MSE):", -grid_search.best_score_)
The most successful of these are taken and used in the model
"""

# Starting model
rf_model = RandomForestRegressor(bootstrap=True, max_depth=10, max_features='sqrt', max_samples=0.8, min_samples_leaf=1, min_samples_split=10, n_estimators=200, random_state=42)

# Fitting data
rf_model.fit(X_train, y_train)

# Creating a prediction
y_pred = rf_model.predict(X_test)

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

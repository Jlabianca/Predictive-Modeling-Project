# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the Boston Housing dataset
boston = load_boston()
data = pd.DataFrame(boston.data, columns=boston.feature_names)
data['PRICE'] = boston.target

# Add a synthetic temporal component
np.random.seed(0)
data['YEAR'] = np.random.choice(range(2000, 2021), size=len(data))

# Feature Engineering: Adjusted price based on average price per year
avg_price_per_year = data.groupby('YEAR')['PRICE'].transform('mean')
data['PRICE_ADJ'] = data['PRICE'] / avg_price_per_year

# Exploratory Data Analysis
plt.figure(figsize=(10, 6))
sns.lineplot(data=data, x='YEAR', y='PRICE_ADJ')
plt.title('Adjusted Housing Prices Over Years')
plt.savefig('adjusted_prices_over_years.png')
plt.show()

# Model Training
X = data.drop(columns=['PRICE', 'PRICE_ADJ'])
y = data['PRICE_ADJ']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Feature Importance
feature_importance = pd.Series(model.coef_, index=X.columns)
feature_importance.nlargest(10).plot(kind='barh')
plt.title('Top 10 Important Features')
plt.savefig('top_10_important_features.png')
plt.show()

# Export Data for Tableau
data['PREDICTED_PRICE'] = model.predict(X)
data.to_csv('boston_housing_predictions.csv', index=False)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('boston_housing_predictions.csv')

plt.figure(figsize=(12, 6))
sns.histplot(data, x='PRICE_ADJ', bins=30, kde=True)
plt.title('Distribution of Adjusted Housing Prices')
plt.savefig('price_distribution.png')
plt.show()

plt.figure(figsize=(12, 6))
sns.boxplot(data=data, x='YEAR', y='PRICE_ADJ')
plt.title('Box Plot of Adjusted Prices Over Years')
plt.savefig('boxplot_adjusted_prices.png')
plt.show()

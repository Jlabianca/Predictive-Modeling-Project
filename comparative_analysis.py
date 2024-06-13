import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('boston_housing_predictions.csv')

plt.figure(figsize=(10, 6))
plt.scatter(data['PRICE_ADJ'], data['PREDICTED_PRICE'], alpha=0.5)
plt.plot([0, 1], [0, 1], '--', color='red', transform=plt.gca().transAxes)
plt.xlabel('Actual Adjusted Price')
plt.ylabel('Predicted Price')
plt.title('Actual vs Predicted Adjusted Prices')
plt.savefig('actual_vs_predicted.png')
plt.show()

data['RESIDUAL'] = data['PRICE_ADJ'] - data['PREDICTED_PRICE']
plt.figure(figsize=(10, 6))
sns.histplot(data['RESIDUAL'], bins=30, kde=True)
plt.title('Distribution of Residuals')
plt.savefig('residual_distribution.png')
plt.show()

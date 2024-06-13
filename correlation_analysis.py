import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('boston_housing_predictions.csv')
correlation_matrix = data.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.savefig('correlation_matrix.png')
plt.show()

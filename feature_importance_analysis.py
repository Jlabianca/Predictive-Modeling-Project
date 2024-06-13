import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

data = pd.read_csv('boston_housing_predictions.csv')
X = data.drop(columns=['PRICE', 'PRICE_ADJ', 'PREDICTED_PRICE'])
y = data['PRICE_ADJ']

model = RandomForestRegressor()
model.fit(X, y)

feature_importance = pd.Series(model.feature_importances_, index=X.columns)
feature_importance.nlargest(10).plot(kind='barh')
plt.title('Top 10 Important Features')
plt.savefig('feature_importance.png')
plt.show()

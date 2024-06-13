import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Load the dataset
data = pd.read_csv('boston_housing_predictions.csv')

# Ensure the YEAR column is in datetime format
data['YEAR'] = pd.to_datetime(data['YEAR'], format='%Y')

# Set the YEAR column as the index and set the frequency
data.set_index('YEAR', inplace=True)
data = data.asfreq('Y')  # Set frequency to yearly

# Perform seasonal decomposition
result = seasonal_decompose(data['PRICE_ADJ'], model='additive')

# Plot the decomposition
result.plot()
plt.suptitle('Seasonal Decomposition of Adjusted Housing Prices', fontsize=16)
plt.savefig('time_series_decomposition.png')
plt.show()

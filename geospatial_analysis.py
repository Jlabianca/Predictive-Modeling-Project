import pandas as pd
import numpy as np  # Ensure numpy is imported
import folium

# Load the dataset
data = pd.read_csv('boston_housing_predictions.csv')

# Example coordinates (not present in the actual Boston Housing dataset)
# For demonstration, we add random latitude and longitude values within the Boston area
np.random.seed(0)
data['LAT'] = np.random.uniform(low=42.2, high=42.4, size=len(data))
data['LON'] = np.random.uniform(low=-71.2, high=-71.0, size=len(data))

# Initialize a Folium map centered around Boston
m = folium.Map(location=[42.3601, -71.0589], zoom_start=12)

# Add CircleMarkers to the map
for _, row in data.iterrows():
    folium.CircleMarker(
        location=[row['LAT'], row['LON']],
        radius=5,
        popup=f"Price: ${row['PRICE_ADJ'] * data['PRICE'].mean():,.2f}",
        color='blue' if row['PRICE_ADJ'] > 1 else 'red',
        fill=True,
        fill_color='blue' if row['PRICE_ADJ'] > 1 else 'red'
    ).add_to(m)

# Save the map as an HTML file
m.save('boston_housing_map.html')

# Optionally, display the map in a Jupyter Notebook
# m

# Boston Housing Prediction Project

## Overview
This project aims to predict housing prices using the Boston Housing dataset and determine the best time to buy/rent a house or apartment. 
The analysis includes data preprocessing, exploratory data analysis (EDA), predictive modeling, and visualization using Python and Tableau.

## Files and Directories
- `data_analysis.py`: Data loading, preprocessing, EDA, and predictive modeling.
- `correlation_analysis.py`: Script to perform correlation analysis and visualize the correlation matrix.
- `feature_importance_analysis.py`: Script to analyze feature importance using a Random Forest model.
- `geospatial_analysis.py`: Script to perform geospatial analysis and visualize housing prices on a map.
- `price_distribution_analysis.py`: Script to analyze and visualize the distribution of housing prices.
- `time_series_decomposition.py`: Script to decompose the time series of housing prices.
- `comparative_analysis.py`: Script to compare actual prices versus predicted prices and analyze residuals.
- `boston_housing_predictions.csv`: Dataset with predicted prices, used for all analyses.
- `README.md`: Project documentation.

## Requirements
- Python 3.x
- Libraries: pandas, numpy, matplotlib, seaborn, scikit-learn, folium, statsmodels

## Instructions

### Running the Analysis
1. Ensure you have all the required Python libraries installed.
2. Run the Python scripts in the following order:
    ```bash
    python data_analysis.py
    python correlation_analysis.py
    python feature_importance_analysis.py
    python geospatial_analysis.py
    python price_distribution_analysis.py
    python time_series_decomposition.py
    python comparative_analysis.py
    ```

### Visualization in Tableau
1. Open Tableau and load the `boston_housing_predictions.csv` file.
2. Create visualizations:
    - Time series plots of `PRICE_ADJ` and `PREDICTED_PRICE`.
    - Bar chart for feature importance.
3. Combine visualizations into an interactive dashboard and add filters/parameters as needed.

## Conclusion
This project demonstrates the process of predicting housing prices using machine learning and visualizing the results to determine the best time to buy/rent a house/apartment. Various analyses provide a comprehensive understanding of the factors influencing housing prices and the model's performance.

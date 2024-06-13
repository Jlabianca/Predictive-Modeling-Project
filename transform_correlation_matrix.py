import pandas as pd

# Load the correlation matrix
correlation_matrix = pd.read_csv('correlation_matrix.csv', index_col=0)

# Transform the matrix into long format
correlation_long = correlation_matrix.reset_index().melt(id_vars='index')
correlation_long.columns = ['Variable1', 'Variable2', 'Correlation']

# Save the transformed data to a CSV file
correlation_long.to_csv('correlation_matrix_long.csv', index=False)

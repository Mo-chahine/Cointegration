import numpy as np
import pandas as pd
from statsmodels.tsa.vector_ar.vecm import coint_johansen

# Read the data from the CSV file
data = pd.read_csv('JohansenTest/nassp(2022-2023).csv')

# Extract the price lists of each stock
stock1_prices = data.iloc[:, 0].values
stock2_prices = data.iloc[:, 1].values

# Combine the price lists into a 2D array
price_matrix = np.column_stack((stock1_prices, stock2_prices))

# Perform Johansen test
result = coint_johansen(price_matrix, det_order=0, k_ar_diff=1)

# Extract the test statistics and critical values
test_statistics = result.lr1
critical_values = result.cvt[:, 0]

# Determine the number of cointegrating relationships (rank) at a specific confidence level
confidence_level = 0.05
num_cointegrating_relationships = sum(test_statistics > critical_values)

# Print the results
print("Johansen Test Results:")
print("-------------------------------------")
print(f"Test Statistics:")
for i, stat in enumerate(test_statistics):
    print(f"Test statistic {i+1}: {stat}")
print("-------------------------------------")
print(f"Critical Values (0.05 significance level):")
print(f"If test statistics 1 and 2 are each greater than critical values 1 and 2, then the 2 are cointegrated")

for i, crit_val in enumerate(critical_values):
    print(f"Critical value {i+1}: {crit_val}")
print("-------------------------------------")
print(f"Number of Cointegrating Relationships: {num_cointegrating_relationships}")
print("-------------------------------------")

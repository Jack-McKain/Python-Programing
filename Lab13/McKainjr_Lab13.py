import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Function to simulate the balls into bins problem for a given N
def simulate_balls_into_bins(N):
    bins = np.zeros(N)
    balls = np.random.randint(0, N, N)
    np.add.at(bins, balls, 1)
    return np.count_nonzero(bins)

# Running the simulation for N from 1 to 1000
N_values = range(1, 1001)
non_empty_bins = [simulate_balls_into_bins(N) for N in N_values]

# Plotting the results
plt.figure(figsize=(10, 5))
plt.plot(N_values, non_empty_bins, marker='o', linestyle='-', markersize=2, label='Non-Empty Bins vs. N')
plt.xlabel('N (Number of Bins and Balls)')
plt.ylabel('Number of Non-Empty Bins')
plt.title('Monte Carlo')
plt.legend()
plt.grid(True)
plt.show()

# Performing linear regression
slope, intercept, r_value, p_value, std_err = linregress(N_values, non_empty_bins)

# Printing the results of the linear regression
print("SciPy Linear Regression Solution")
print(f" slope: {slope}")
print(f" intercept: {intercept}")
print(f" rvalue: {r_value}")

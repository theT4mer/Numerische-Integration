import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the data (adjust the path as needed)
dataframe = pd.read_csv('src/Daten_TV.txt', header=None)  # just replace with your path
data_points = dataframe.values
n = len(data_points)

# Calculate the mean (arithmetic mean)
mean_value = 0
for i in range(1, n):  # index starts at 1 in your original code
    mean_value += data_points[i, 0]

mean_value = mean_value / n  # arithmetic mean

# Pass the mean to a variable mu
mu = mean_value

# Calculate the variance
variance = data_points[0, 0]**2 - mean_value**2
for i in range(1, n):
    variance += data_points[i, 0]**2 - mean_value**2

variance = variance / (n - 1)  # unbiased variance

# Trapezoidal rule to find the value c from the standard normal distribution
# Given density function: phi(u) = 1/sqrt(2*pi) * exp(-0.5*u^2)

gamma = 0.9  # Example value for gamma; you can adjust as needed
step_size = 0.001
area = 0.5
start = 0
end = step_size
target_area = (gamma + 1) / 2

while area < target_area:
    # Trapezoidal rule
    area += step_size / 2 * (1 / np.sqrt(2 * np.pi) * np.exp(-0.5 * start**2) +
                             1 / np.sqrt(2 * np.pi) * np.exp(-0.5 * end**2))
    start += step_size
    end += step_size

# The desired c-value
c_value = start
print(f"The value of c is: {c_value}")

# Plot the data points
plt.figure(figsize=(10, 6))
plt.plot(range(len(data_points)), data_points, 'ro')
plt.xlabel('Index')
plt.ylabel('Beautiful Values')
plt.title("Gerky's Great and Wonderful Data")
plt.grid()
plt.show()

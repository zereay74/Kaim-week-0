# Import necessary libraries
import random
import matplotlib.pyplot as plt
import numpy as np

# Set a seed for reproducibility
random.seed(42)

# Generate a list of 50 random integers between 0 and 100
random_numbers = [random.randint(0, 100) for _ in range(50)]

# Calculate basic statistics
mean_value = np.mean(random_numbers)
median_value = np.median(random_numbers)
std_dev = np.std(random_numbers)

# Identify outliers (consider outliers as values greater than mean + 2 * std deviation)
outliers = [x for x in random_numbers if x > mean_value + 2 * std_dev]

# Print statistics
print("Generated Numbers: ", random_numbers)
print("Mean:", mean_value)
print("Median:", median_value)
print("Standard Deviation:", std_dev)
print("Outliers:", outliers)

# Plot the histogram of the generated numbers
plt.figure(figsize=(10, 6))
plt.hist(random_numbers, bins=10, color='lightblue', edgecolor='black', label='Random Data')
plt.axvline(mean_value, color='red', linestyle='dashed', linewidth=1, label='Mean')
plt.title('Histogram of Random Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()
plt.grid()
plt.show()

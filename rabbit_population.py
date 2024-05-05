import numpy as np
import matplotlib.pyplot as plt

# Parameters
num_trials = 100  # Number of trials (years)
num_rabbits_initial = 10  # Initial number of rabbits
survival_rate = 0.25  # Probability of survival for each rabbit in a year
growth_rate = 6  # Average number of offspring per surviving rabbit after one year

# Simulate survival over the year
survival_results = np.random.binomial(num_rabbits_initial, survival_rate, num_trials)

# Simulate growth after surviving a year
growth_results = survival_results * growth_rate

# Plotting the results
plt.figure(figsize=(10, 6))

# Plot survival distribution
plt.subplot(2, 1, 1)
plt.hist(survival_results, bins=np.arange(min(survival_results), max(survival_results) + 1), density=True, color='blue', alpha=0.7)
plt.title('Distribution of Surviving Rabbits after One Year')
plt.xlabel('Number of Surviving Rabbits')
plt.ylabel('Probability')

# Plot growth distribution
plt.subplot(2, 1, 2)
plt.hist(growth_results, bins=np.arange(min(growth_results), max(growth_results) + 1), density=True, color='green', alpha=0.7)
plt.title('Distribution of Rabbit Growth after One Year')
plt.xlabel('Number of Offspring')
plt.ylabel('Probability')

plt.tight_layout()
plt.show()

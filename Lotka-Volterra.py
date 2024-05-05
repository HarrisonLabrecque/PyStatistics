import numpy as np
import matplotlib.pyplot as plt

# Parameters
alpha = 0.1  # Prey growth rate
beta = 0.02  # Predation rate
gamma = 0.3  # Predator reproduction rate
delta = 0.01  # Predator death rate

# Initial populations
prey_population = 50
predator_population = 20

# Simulation settings
num_steps = 100  # Number of time steps

# Arrays to store populations over time
prey_population_over_time = np.zeros(num_steps)
predator_population_over_time = np.zeros(num_steps)

# Initial population values
prey_population_over_time[0] = prey_population
predator_population_over_time[0] = predator_population

# Gillespie algorithm for stochastic simulation
for t in range(1, num_steps):
    # Compute reaction rates
    prey_birth_rate = alpha * prey_population_over_time[t - 1]
    predation_rate = beta * prey_population_over_time[t - 1] * predator_population_over_time[t - 1]
    predator_death_rate = delta * predator_population_over_time[t - 1]
    predator_birth_rate = gamma * predation_rate
    
    # Total reaction rate
    total_rate = prey_birth_rate + predation_rate + predator_death_rate + predator_birth_rate
    
    # Check if total rate is zero
    if total_rate == 0:
        # If total rate is zero, populations remain unchanged
        prey_population_over_time[t] = prey_population_over_time[t - 1]
        predator_population_over_time[t] = predator_population_over_time[t - 1]
        continue
    
    # Time until next event
    dt = np.random.exponential(1 / total_rate)
    
    # Determine which event occurs
    probabilities = [prey_birth_rate, predation_rate, predator_death_rate, predator_birth_rate]
    probabilities = [max(p, 0) for p in probabilities]  # Ensure probabilities are non-negative
    probabilities /= np.sum(probabilities)  # Normalize probabilities
    event = np.random.choice(range(4), p=probabilities)
    
    # Update populations accordingly
    if event == 0:
        prey_population_over_time[t] = prey_population_over_time[t - 1] + 1
        predator_population_over_time[t] = predator_population_over_time[t - 1]
    elif event == 1:
        prey_population_over_time[t] = prey_population_over_time[t - 1] - 1
        predator_population_over_time[t] = predator_population_over_time[t - 1] + 1
    elif event == 2:
        prey_population_over_time[t] = prey_population_over_time[t - 1]
        predator_population_over_time[t] = predator_population_over_time[t - 1] - 1
    elif event == 3:
        prey_population_over_time[t] = prey_population_over_time[t - 1] + 1
        predator_population_over_time[t] = predator_population_over_time[t - 1] + 1

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(range(num_steps), prey_population_over_time, label='Prey')
plt.plot(range(num_steps), predator_population_over_time, label='Predator')
plt.title('Lotka-Volterra Model (Stochastic)')
plt.xlabel('Time Steps')
plt.ylabel('Population')
plt.legend()
plt.grid(True)
plt.show()

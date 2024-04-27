import numpy as np
import matplotlib.pyplot as plt

# This function simulates the Galton-Watson process for language learning over multiple generations.
def galton_watson_language_learning(num_generations_list, initial_learners_list, offspring_mean, transmission_probability):
    results = {}  # Initialize a dictionary to store simulation results
    for initial_learners in initial_learners_list:  # Loop over different initial learner counts
        initial_results = {}  # Initialize a dictionary for results with this initial learner count
        for num_generations in num_generations_list:  # Loop over different numbers of generations
            learners_per_generation = [initial_learners]  # Start with the initial number of learners
            extinction_probabilities = []  # Initialize a list to store extinction probabilities
            
            # Iterate over each generation, excluding the first (already initialized)
            for gen in range(num_generations - 1):
                # Generate offspring counts for each learner in the current generation
                offspring_counts = np.random.poisson(offspring_mean, learners_per_generation[-1])
                # Calculate the number of new learners based on transmission probability
                new_learners = np.sum(np.random.rand(offspring_counts.sum()) < transmission_probability)
                # Calculate extinction probability for the current generation
                extinction_prob = np.sum(offspring_counts == 0) / len(offspring_counts)
                extinction_probabilities.append(extinction_prob)  # Add extinction probability to the list
                learners_per_generation.append(new_learners)  # Add new learners to the list
            initial_results[num_generations] = (learners_per_generation, extinction_probabilities)  # Store results for this number of generations
        results[initial_learners] = initial_results  # Store results for this initial learner count
    return results  # Return the dictionary containing all simulation results

# Example usage
num_generations_list = [10, 20, 30]  # List of numbers of generations to simulate
initial_learners_list = [5, 10, 15]  # List of initial learners
offspring_mean = 3  # Mean number of offspring
transmission_probability = 0.5  # Probability of passing language skills to offspring

# Perform the simulation
results = galton_watson_language_learning(num_generations_list, initial_learners_list, offspring_mean, transmission_probability)

# Plotting number of learners over generations
plt.figure(figsize=(12, 6))
for initial_learners in initial_learners_list:
    for num_generations in num_generations_list:
        result, _ = results[initial_learners][num_generations]  # Extract learner counts for this combination
        plt.plot(range(1, num_generations + 1), result, marker='o', label=f'Initial Learners: {initial_learners}, Generations: {num_generations}')  # Plot learner counts
        
plt.title('Number of Learners Over Generations and Extinction Probability')
plt.xlabel('Generation')
plt.ylabel('Number of Learners')
plt.grid(True)
plt.legend()
plt.show()

# Plotting histogram of extinction probabilities
plt.figure(figsize=(8, 6))
for initial_learners in initial_learners_list:
    for num_generations in num_generations_list:
        _, extinction_probs = results[initial_learners][num_generations]  # Extract extinction probabilities for this combination
        plt.hist(extinction_probs, bins=20, alpha=0.5, label=f'Initial Learners: {initial_learners}, Generations: {num_generations}')  # Plot histogram
        
plt.title('Histogram of Extinction Probabilities')
plt.xlabel('Extinction Probability')
plt.ylabel('Frequency')
plt.grid(True)
plt.legend()
plt.show()

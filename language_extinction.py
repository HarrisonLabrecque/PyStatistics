import numpy as np
import matplotlib.pyplot as plt

all_extinction_probs =[] 

#This function simulates language learning using the Galton-Watson process.
def galton_watson_language_learning(num_generations, initial_learners, offspring_mean, transmission_probability):
    learners_per_generation = [initial_learners]
    extinction_probabilities = []
    #It iterates through each generation, calculates the number of new learners 
    for gen in range(num_generations - 1):
        offspring_counts = np.random.poisson(offspring_mean, learners_per_generation[-1])
        new_learners = np.sum(np.random.rand(offspring_counts.sum()) < transmission_probability)
        extinction_prob = np.sum(offspring_counts == 0) / len(offspring_counts)
        extinction_probabilities.append(extinction_prob)
        learners_per_generation.append(new_learners)
    return learners_per_generation, extinction_probabilities

# Example usage
num_generations = [2,4,8,10]
initial_learners_list = [5, 10, 20]
offspring_mean = 2 # Mean number of offspring
transmission_probability = 0.5 # Probability of passing language skills to offspring

plt.figure(figsize=(12, 6))

for initial_learners in initial_learners_list:
    result, extinction_probs = galton_watson_language_learning(num_generations, initial_learners, offspring_mean, transmission_probability)
    plt.plot(range(1, num_generations + 1), result, marker='o', label=f'Initial Learners: {initial_learners}')
    #plt.plot(range(1, num_generations), extinction_probs, marker='x', linestyle='--')

    # Collect extinction probabilities for histogram
    all_extinction_probs.extend(extinction_probs)

plt.title('Number of Learners Over Generations')
plt.xlabel('Generation')
plt.ylabel('Number of Learners')
plt.grid(True)
plt.legend()
plt.show()

# Plotting the histogram of extinction probabilities
plt.figure(figsize=(8, 6))
plt.hist(all_extinction_probs, bins=20, density=True)
plt.title('Histogram of Extinction Probabilities')
plt.xlabel('Extinction Probability')
plt.ylabel('Density')
plt.grid(True)
plt.show()

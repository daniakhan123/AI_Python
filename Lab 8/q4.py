import numpy as np
import random

# Step 1: Define the weather states
states = ['Sunny', 'Cloudy', 'Rainy']
state_to_index = {state: i for i, state in enumerate(states)}

# Step 2: Define the transition probability matrix
# Rows = From state, Columns = To state
transition_matrix = [
    [0.6, 0.3, 0.1],  # From Sunny
    [0.2, 0.5, 0.3],  # From Cloudy
    [0.3, 0.3, 0.4]   # From Rainy
]

# Step 3: Simulate the weather for 10 days starting with 'Sunny'
def simulate_weather(start_state='Sunny', days=10):
    current_state = state_to_index[start_state]
    weather_sequence = [start_state]

    for _ in range(days - 1):
        next_state = np.random.choice(
            states, p=transition_matrix[current_state])
        weather_sequence.append(next_state)
        current_state = state_to_index[next_state]

    return weather_sequence

# Step 4: Run multiple simulations and estimate P(at least 3 rainy days in 10)
def estimate_rainy_days_probability(simulations=10000):
    count_with_3_or_more_rainy_days = 0

    for _ in range(simulations):
        sequence = simulate_weather()
        rainy_days = sequence.count('Rainy')
        if rainy_days >= 3:
            count_with_3_or_more_rainy_days += 1

    probability = count_with_3_or_more_rainy_days / simulations
    return probability

# Run a single 10-day simulation and show result
single_sequence = simulate_weather()
print("10-day weather sequence (starting Sunny):")
print(single_sequence)

# Estimate probability using simulation
estimated_prob = estimate_rainy_days_probability()
print(f"\nEstimated P(at least 3 Rainy days in 10): {estimated_prob:.4f}")

import numpy as np
import matplotlib.pyplot as plt
import random

# Number of cities and their coordinates
num_cities = 10
cities = np.random.rand(num_cities, 2)

# Calculate total distance of a route
def route_distance(route):
    return sum(np.linalg.norm(cities[route[i]] - cities[route[(i + 1) % num_cities]]) for i in range(num_cities))

# Create initial population
def initial_population(pop_size):
    return [random.sample(range(num_cities), num_cities) for _ in range(pop_size)]

# Rank population by fitness (shorter distance is better)
def rank_routes(population):
    return sorted(population, key=lambda r: route_distance(r))

# Select parents using elitism and roulette wheel selection
def select_parents(population, elite_size):
    ranked = rank_routes(population)
    fitness_scores = [1 / route_distance(route) for route in ranked]
    prob = np.array(fitness_scores) / sum(fitness_scores)

    selected = ranked[:elite_size]
    selected_indices = np.random.choice(len(ranked), len(ranked) - elite_size, p=prob, replace=False)
    selected += [ranked[i] for i in selected_indices]
    return selected

# Ordered Crossover (OX)
def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(num_cities), 2))
    child = [-1] * num_cities
    child[start:end] = parent1[start:end]
    fill = [city for city in parent2 if city not in child]
    idx = 0
    for i in range(num_cities):
        if child[i] == -1:
            child[i] = fill[idx]
            idx += 1
    return child
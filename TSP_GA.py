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

# Mutation (swap cities)
def mutate(route, mutation_rate):
    for i in range(num_cities):
        if random.random() < mutation_rate:
            j = random.randint(0, num_cities - 1)
            route[i], route[j] = route[j], route[i]
    return route

# Create next generation
def next_generation(current_gen, elite_size, mutation_rate):
    parents = select_parents(current_gen, elite_size)
    children = [crossover(parents[i], parents[-i-1]) for i in range(len(current_gen))]
    return [mutate(child, mutation_rate) for child in children]

# Run the Genetic Algorithm
def run_ga(generations=100, pop_size=100, elite_size=20, mutation_rate=0.01):
    population = initial_population(pop_size)
    best_route = rank_routes(population)[0]
    best_distance = route_distance(best_route)

    for _ in range(generations):
        population = next_generation(population, elite_size, mutation_rate)
        current_best = rank_routes(population)[0]
        current_distance = route_distance(current_best)
        if current_distance < best_distance:
            best_distance = current_distance
            best_route = current_best

    return best_route, best_distance

# Run and visualize
best_route, best_distance = run_ga()
best_path = cities[best_route + [best_route[0]]]

plt.figure(figsize=(10, 6))
plt.plot(best_path[:, 0], best_path[:, 1], 'o-', color='blue')
plt.title(f'Shortest Route Found (Distance = {best_distance:.4f})')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.grid(True)
plt.show()
# Genetic-TSP-Solver 
This project demonstrates how to solve the **Traveling Salesman Problem (TSP)** using a **Genetic Algorithm (GA)** implemented in Python. The TSP is a classic optimization problem in which the goal is to find the shortest possible route that visits a set of cities exactly once and returns to the starting point.
# Genetic-TSP-Solver 🧬📍

This project demonstrates how to solve the **Traveling Salesman Problem (TSP)** using a **Genetic Algorithm (GA)** implemented in Python. The TSP is a classic optimization problem in which the goal is to find the shortest possible route that visits a set of cities exactly once and returns to the starting point.

## 🚀 Features

- Random generation of cities
- Genetic Algorithm with:
  - Elitism selection
  - Roulette wheel selection
  - Ordered Crossover (OX)
  - Mutation via city swapping
- Visualizes the best path found
- Adjustable parameters: population size, mutation rate, elite size, and number of generations

## 🧠 Algorithm Overview

The Genetic Algorithm mimics natural selection to iteratively evolve a better route:
1. **Initialization**: Random routes (permutations of cities) form the initial population.
2. **Selection**: Fitter routes (shorter total distances) are more likely to be chosen.
3. **Crossover**: Parents produce children by combining sequences.
4. **Mutation**: Small random changes maintain genetic diversity.
5. **Repeat**: The best route evolves over generations.
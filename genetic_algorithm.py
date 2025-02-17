import numpy as np
import random

import plotter
from config import *
import provider

"""
    Create an initial population of random routes (permutations of city indices).

    Args:
        cities: List of cities.
        populationSize: Number of individuals in the population.

    Returns:
        A list containing random permutations of city indices.
    """

def createInitialPopulation(cities, populationSize) -> list:
    population = []
    for i in range(populationSize):
        population.append(np.random.permutation(len(cities)))
    return population


"""
    Perform tournament selection on the population.

    Args:
        population: Current population of routes.
        fitness: Corresponding fitness values for each route.

    Returns:
        The top individuals from a random sample of the population.
    """

def tournamentSelection(population, fitness):
    return sorted(random.sample(list(zip(population, fitness)), 5), key = lambda x: -x[1])


"""
    Selects the best individuals from the population based on fitness.

    Args:
        population: Current population of routes.
        fitness: Corresponding fitness values for each route.

    Returns:
        A sorted list of the population based on fitness.
    """

def bestSelection(population, fitness):
    return sorted(list(zip(population, fitness)), key = lambda x: -x[1])


"""
    Perform crossover between two parent routes to create a child route.

    Args:
        cities: List of cities.
        parent1: First parent route.
        parent2: Second parent route.

    Returns:
        A new child route created from the parents.
    """

def crossover(cities, parent1, parent2):

    citiesLen = len(cities)

    start, end = sorted(random.sample(range(citiesLen), 2))
    child = [-1] * citiesLen
    child[start:end] = parent1[start:end]

    index = end

    for gene in parent2:
        if gene not in child:
            if index == citiesLen:
                index = 0
            child[index] = gene
            index += 1

    return child


"""
    Mutate the child route with a given mutation probability.

    Args:
        child: The child route to mutate.
        probability: Probability of mutation for each city in the route.

    Returns:
        The mutated child route.
    """

def mutate(child, probability):
    size = len(child)
    for i in range(size):
        if random.random() < probability:
            j = (i + 1) % size
            child[i], child[j] = child[j], child[i]
    return child


def main(cities):
    print("GENETIC ALGORITHM\n" + "_" * 20)

    # Create the initial population
    initialPopulation = createInitialPopulation(cities, POPULATION)
    # Find the best route in the initial population
    bestRoute = min(initialPopulation, key=lambda x: provider.routeLength(cities, x))

    oldBestRoute = provider.routeLength(cities, bestRoute)

    # Keep track of the best routes
    bestRoutes = [bestRoute]

    progress = []

    # Evolve the population over a specified number of generations
    for generation in range(GENERATIONS):

        # Calculate fitness for the current population
        fitness = [1 / provider.routeLength(cities, population) for population in initialPopulation]
        newGeneration = []
        for _ in range(POPULATION):
            # Select parents using either tournament or best selection
            selection = tournamentSelection(initialPopulation, fitness) if random.random() < 0.5 else bestSelection(
                initialPopulation, fitness)

            parent1, parent2 = selection[0][0], selection[1][0]

            # Generate a child from the parents
            child = crossover(cities, parent1, parent2)
            # Mutate the child with a given probability
            child = mutate(child, MUTATION_PROBABILITY)
            # Add the child to the new generation
            newGeneration.append(child)

        # Update the population for the next generation
        initialPopulation = newGeneration
        # Find the best route in the new population
        temp = min(initialPopulation, key=lambda x: provider.routeLength(cities, x))

        # Update the overall best route found so far
        bestRoute = min(temp, bestRoute, key=lambda x: provider.routeLength(cities, x))

        progress.append(provider.routeLength(cities, bestRoute))

        # If a better route is found, update the old best route
        if provider.routeLength(cities, bestRoute) < oldBestRoute:
            oldBestRoute = provider.routeLength(cities, bestRoute)
            bestRoutes.append(bestRoute)

        # Print progress every 100 generations
        if (generation + 1) % 100 == 0:
            print(f"Generation {generation} - Best route length: {provider.routeLength(cities, bestRoute)}")
            print(f"Temp: {provider.routeLength(cities, temp)}")

    print(f"Best route found: {bestRoute}")
    print(f"Shortest distance: {provider.routeLength(cities, bestRoute)}")


    plotter.plot_evaluation(progress, len(progress), max(progress) + 10, "Genetic Algorithm Evaluation")

    return bestRoutes
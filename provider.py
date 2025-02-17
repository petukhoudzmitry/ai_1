import numpy as np
import config

def generateCities():
    return np.random.randint(0, config.MAP_SIZE, size = (np.random.randint(config.MIN_NUM_CITIES, config.MAX_NUM_CITIES + 1), 2))

def distance(a, b) -> float:
    return np.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def routeLength(cities, route) -> float:
    length = 0.0
    for i in range(len(route)):
        length += distance(cities[route[i]], cities[route[(i + 1) % len(cities)]])
    return length
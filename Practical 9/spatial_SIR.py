# Pseudocode:
# 1. Create a 100x100 grid (0=S, 1=I, 2=R)
# 2. Pick a random (x, y) to start the infection
# 3. Loop through 100 time steps:
#    a. Find all currently infected cells (value == 1)
#    b. For each infected cell, try to infect its 8 neighbors (if they are S)
#    c. For each infected cell, try to recover (becomes 2)
#    d. Display the grid at intervals (0, 10, 50, 100)

import numpy as np
import matplotlib.pyplot as plt

width, height = 100, 100
beta = 0.3
gamma = 0.05
steps = 100

# 0: Susceptible, 1: Infected, 2: Recovered
population = np.zeros((width, height))

# Random initial outbreak
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1

for t in range(steps + 1):
    # Visualize at specific steps
    if t in [0, 10, 50, 100]:
        plt.figure()
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title(f"Time Step: {t}")
        plt.show()

    new_population = population.copy()
    
    infected_coords = np.where(population == 1)
    
    for i in range(len(infected_coords[0])):
        x, y = infected_coords[0][i], infected_coords[1][i]
        
        # 1. Attempt to infect neighbors (8-neighbor rule)
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                # Check grid boundaries
                if 0 <= nx < width and 0 <= ny < height:
                    if population[nx, ny] == 0:
                        if np.random.random() < beta:
                            new_population[nx, ny] = 1
                            
        if np.random.random() < gamma:
            new_population[x, y] = 2
            
    population = new_population
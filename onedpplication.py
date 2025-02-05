import numpy as np
import matplotlib.pyplot as plt

def rule_250(cells):
    new_configuration = np.zeros_like(cells)
    cells = cells.astype(int) 
    
    for i in range(1, len(cells) - 1):
        neighborhood = (cells[i-1] << 2) | (cells[i] << 1) | cells[i+1]
        new_configuration[i] = (250 >> neighborhood) & 1
    
    return new_configuration

def simulate_automaton(initial_cells, num_generations):
    cells = initial_cells.copy().astype(int)
    evolutions = [cells.copy()]
    
    for _ in range(num_generations):
        cells = rule_250(cells)
        evolutions.append(cells.copy())
        
    return evolutions

n = 128  #number of cells
num_generations = 64  #number of generations
initial_cells = np.zeros(n, dtype=int)
initial_cells[n // 2] = 1  #initial point

evolutions = simulate_automaton(initial_cells, num_generations)

evolutions = np.array(evolutions)

plt.figure(figsize=(12, 8))
for i in range(10, num_generations + 1, 10):
    plt.subplot(3, 2, i // 10)
    plt.imshow(evolutions[:i], cmap='binary', interpolation='nearest', aspect='auto')
    plt.title(f"Evolution up to Generation {i}")
    plt.xlabel("Position Along the Coast")
    plt.ylabel("Generation")

plt.tight_layout() 
plt.show()

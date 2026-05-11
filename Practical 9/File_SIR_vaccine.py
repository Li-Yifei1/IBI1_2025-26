# Pseudocode:
# 1. Define a list of vaccination rates: 0%, 10%, ..., 100%
# 2. For each rate, run the SIR simulation
# 3. Initially: V = N * rate, S = N - V - 1, I = 1, R = 0
# 4. Only record the "Infected" history for comparison
# 5. Plot all Infected curves on one graph using a colormap

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

N = 10000
beta = 0.3
gamma = 0.05
time_steps = 1000
vaccination_rates = np.linspace(0, 1, 11)

plt.figure(figsize=(6, 4), dpi=150)

# Loop through different vaccination levels
for i, rate in enumerate(vaccination_rates):
    # Initial state adjusted for vaccination
    V = int(N * rate)
    if V == N:
        S = 0 
        I = 0
    else:
        I = 1
        S = N - V - 1
        R = 0
    
    i_history = [I]
    
    for t in range(time_steps):
        prob_inf = beta * (I / N)
        
        # Stochastic changes
        num_new_inf = np.sum(np.random.choice(range(2), size=S, p=[1 - prob_inf, prob_inf]))
        num_new_rec = np.sum(np.random.choice([0, 1], size=I, p=[1 - gamma, gamma]))
        
        S -= num_new_inf
        I += num_new_inf - num_new_rec
        R += num_new_rec
        
        i_history.append(I)
    
    # Plot infected curve for this rate
    plt.plot(i_history, label=f'{int(rate*100)}%', color=cm.viridis(i/10))

plt.title("SIR model with different vaccination rates")
plt.xlabel("time")
plt.ylabel("number of people")
plt.legend(loc='upper right', fontsize='small')
plt.savefig('Fig.SIR.vaccine.png', format="png")
plt.show()
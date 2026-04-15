# Pseudocode:
# 1. Import (numpy and matplotlib)
# 2. Set initial parameters: N=10000, beta=0.3, gamma=0.05
# 3. Initial state: 1 Infected, 0 Recovered, 9999 Susceptible
# 4. Create lists to store the history of S, I, and R
# 5. Loop through 1000 time steps:
#    a. Calculate probability of infection: beta * (Infected / Total)
#    b. For each Susceptible person, decide if they become Infected
#    c. For each Infected person, decide if they become Recovered
#    d. Update counts and record them
# 6. Plot the results over time

import numpy as np
import matplotlib.pyplot as plt

# Define basic variables
N = 10000
beta = 0.3
gamma = 0.05
time_steps = 1000

# Initial numbers
S = 9999
I = 1
R = 0

# Lists to track evolution
s_history = [S]
i_history = [I]
r_history = [R]

# Time course loop
for t in range(time_steps):
    # Calculate current probability of a susceptible person meeting an infected one
    prob_inf = beta * (I / N)
    
    new_infections = np.random.choice(range(2), size=S, p=[1 - prob_inf, prob_inf])
    num_new_inf = np.sum(new_infections)
    
        # 1 = recovers, 0 = stays infected
    new_recoveries = np.random.choice(range(2), size=I, p=[1 - gamma, gamma])
    num_new_rec = np.sum(new_recoveries)
    
    # Update current counts
    S = S - num_new_inf
    I = I + num_new_inf - num_new_rec
    R = R + num_new_rec
    
    s_history.append(S)
    i_history.append(I)
    r_history.append(R)

# Plotting the results
plt.figure(figsize=(6, 4), dpi=150)
plt.plot(s_history, label='Susceptible')
plt.plot(i_history, label='Infected')
plt.plot(r_history, label='Recovered')
plt.title("SIR model")
plt.xlabel("time")
plt.ylabel("number of people")
plt.legend()
plt.savefig ('Fig.SIR.png',  format="png")
plt.show()

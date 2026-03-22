# Import required libraries
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Store population data, calculate percentage change and print results
pop_2020 = {'UK': 66.7, 'China': 1426, 'Italy': 59.4, 'Brazil': 208.6, 'USA': 331.6}
pop_2024 = {'UK': 69.2, 'China': 1410, 'Italy': 58.9, 'Brazil': 212.0, 'USA': 340.1}

# Initialize dictionary to store percentage change
pop_change = {}
for country in pop_2020.keys():
    # Calculate percentage change using formula: ((pop_2024 - pop_2020)/pop_2020) * 100
    change = (pop_2024[country] - pop_2020[country]) / pop_2020[country] * 100
    pop_change[country] = round(change, 2)  # Round to 2 decimal places

# Print country-wise percentage change
print(" Population Percentage Change (2020-2024) :")
for country, rate in pop_change.items():
    if rate > 0:
        print(country,":+",rate,"%")
    elif rate < 0:
        print(country,":",rate,"%")
    else:
        print(country,":", "No change")

# Step 2: Sort changes in descending order and identify extreme countries
# Sort items by change rate (descending order)
sorted_change = sorted(pop_change.items(), key=lambda x: x[1], reverse=True)
# Print sorted results
print(" Population Change Sorted (Highest Growth to Highest Decrease): ")
for idx, (country, rate) in enumerate(sorted_change, 1):
    if rate > 0:
        print(idx,".", country,":","+",rate,"%")
    elif rate < 0:
        print(idx,".", country,":",rate,"%")
    else:
        print(idx,".", country,": No change")

# Identify countries with maximum growth and maximum decrease
max_grow_country, max_grow_rate = sorted_change[0]
max_decrease_country, max_decrease_rate = sorted_change[-1]
print(" Extreme Population Change Countries :")
print("Country with highest population growth:", max_grow_country, "+",max_grow_rate,"%")
print("Country with highest population decrease:",max_decrease_country,max_decrease_rate,"%")

# Step 3: Generate labeled bar chart for sorted population changes
sorted_countries = [c for c, r in sorted_change]  # Extract sorted country names
sorted_rates = [r for c, r in sorted_change]     # Extract sorted change rates
plt.figure(figsize=(8, 9))

# Assign colors: green for growth, red for decrease, gray for no change
colors = ['lightgreen' if r > 0 else 'lightcoral' if r < 0 else 'lightgray' for r in sorted_rates]
bars = plt.bar(sorted_countries, sorted_rates, color=colors)

# Add chart labels, title and grid
plt.title('Population Percentage Change (2020-2024) by Country', fontsize=14)
plt.xlabel('Country', fontsize=12)
plt.ylabel('Population Percentage Change (%)', fontsize=12)

# Add value labels on top/bottom of bars
for bar, rate in zip(bars, sorted_rates):
    height = bar.get_height()
    if rate > 0:
        plt.text(bar.get_x() + bar.get_width()/2, height + 0.1, f"{rate}%", ha='center')
    else:
        plt.text(bar.get_x() + bar.get_width()/2, height - 0.3, f"{rate}%", ha='center')

plt.tight_layout()
plt.show()
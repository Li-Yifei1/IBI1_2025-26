import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("C:/Users/thinkpad/Downloads")
print(os.listdir())
print(os.getcwd())

try:
    dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
    print("====successfully read data====") # exam whether it is successfully read
except:
    print("fail to read")

# Requirement 2
afg_10 = dalys_data.iloc[0:10,2:4]
print("===The first 10 :Years and DALYs===")
print(afg_10)
afg_max = afg_10.loc[afg_10['DALYs'].idxmax()]
afg_max_year = afg_max['Year']
print("The maximum DALYs across the first 10 years for Afghanistan was", int(afg_max_year))
# Based on the head() of the dataset (Afghanistan 1990-1999):
# The year that reported the maximum DALYs across the first 10 years for Afghanistan was 1998.

# Requirement 3
zimbabwe_mask = dalys_data['Entity'] == "Zimbabwe"
zimbabwe_data = dalys_data.loc[zimbabwe_mask,"Year"]
print("===DALY data for Zimbabwe===")
print(zimbabwe_data)
zim_min_year = zimbabwe_data.min()
zim_max_year = zimbabwe_data.max()
print("The year data for zimbabwe range from",zim_min_year,"to",zim_max_year)
# For Zimbabwe, the first year recorded was 1990 
# the last year recorded was 2019.


# Requirement 4

recent_data = dalys_data.loc[dalys_data['Year'] == 2019, ["Entity", "DALYs"]]

max_daly_row = recent_data.loc[recent_data['DALYs'].idxmax()]
min_daly_row = recent_data.loc[recent_data['DALYs'].idxmin()]
max_country = max_daly_row['Entity']
min_country = min_daly_row['Entity']

print("===== Data for 2019 =====")
print(recent_data)
print("In 2019, the country with the maximum DALYs was:", max_country)
print("In 2019, the country with the minimum DALYs was:",min_country)
#In 2019, the country with the maximum DALYs was: Lesotho
#In 2019, the country with the minimum DALYs was: Singapore

# Requirement 5
max_country_data = dalys_data.loc[dalys_data['Entity'] == max_country]

plt.figure(figsize=(10, 6))
plt.plot(max_country_data['Year'], max_country_data['DALYs'], 'r+-', label=max_country)
# Requirement 8: All plots are clearly labeled
plt.xlabel('Year')
plt.ylabel('DALYs (Disability Adjusted Life Years)')
plt.title('Trend of DALYs over time in '+ max_country)
plt.grid(True)
plt.xticks(max_country_data['Year'], rotation=-90)
plt.legend()
plt.tight_layout()
plt.show()
print("The figure of Lesotho 2019 DALYs is shown")

# Requirement 6
# Question: What was the distribution of DALYs across all countries in 2019?
# This starts at line 71
plt.figure(figsize=(8, 5))
plt.hist(recent_data['DALYs'], bins=30, color='skyblue', edgecolor='black')
plt.xlabel('DALY Rate')
plt.ylabel('Number of Countries')
plt.title('Distribution of DALYs across all countries in 2019')
plt.grid(axis='y', alpha=0.75)
plt.show()
print("The figure for 2019 DALYs global distribution is shown")
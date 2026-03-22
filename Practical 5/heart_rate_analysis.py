# Import required libraries
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Store heart rate data, calculate and print patient count and average heart rate
heart_rates = (72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64)
patient_num = len(heart_rates)  # Get total number of patients
mean_hr = np.mean(heart_rates)  # Calculate average heart rate (alternative: sum(heart_rates)/patient_num)
# Print basic dataset information
print(" Basic Heart Rate Dataset Information ")
print("Total patients in dataset:", patient_num, "average resting heart rate:", mean_hr, "bpm")

# Step 2: Categorize and count heart rates by level
low = 0    
normal = 0 
high = 0   

for hr in heart_rates:
    if hr < 60:
        low += 1
    elif 60 <= hr <= 120:
        normal += 1
    else:
        high += 1

# Print category counts
print(" Heart Rate Category Counts ")
print("Low heart rate (<60 bpm):", low ,"patients")
print("Normal heart rate (60-120 bpm):", normal, "patients")
print("High heart rate (>120 bpm):", high, "patients")

# Step 3: Identify and print the most frequent heart rate category
counts = [low, normal, high]
categories = ['Low', 'Normal', 'High']
max_count = max(counts)
max_category = categories[counts.index(max_count)]
print(" Most Frequent Heart Rate Category ")
print("The most frequent category is", max_category, "with", max_count ,"patients")

# Step 4: Generate labeled pie chart for category distribution
plt.figure(figsize=(7, 7))  # Use square figure to ensure circular pie chart
# Explode the largest category for emphasis

colors = ['lightcoral', 'pink', 'lightskyblue']
plt.pie(counts, labels=categories, autopct='%1.1f%%',
        explode = (0.05,0.1,0.05),
        colors=colors, shadow=True, startangle=90)
# Add chart title and ensure circular shape
plt.title('Distribution of Resting Heart Rate Categories', fontsize=14)
plt.axis('equal')  # Force equal aspect ratio to make pie chart circular
plt.show()

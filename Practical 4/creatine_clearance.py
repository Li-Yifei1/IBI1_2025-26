 
# Pseudocode 
# 1. Prompt the user to input age (in years), weight (in kg), Cr (in µmol/l), and gender.
# 2. Create a flag 'is_valid' and set it to True initially.
# 3. Validate age: if age >= 100, print specific error and set is_valid to False.
# 4. Validate weight: if weight <= 20 or weight >= 80, print specific error and set is_valid to False.
# 5. Validate Cr: if Cr <= 0 or Cr >= 100, print specific error and set is_valid to False.
# 6. Validate gender: if not 'male' or 'female', print specific error and set is_valid to False.
# 7. If all inputs are valid (is_valid is True):
# 8.    Calculate CrCl using the Cockcroft-Gault Equation.
# 9.    If gender is 'female', multiply the result by 0.85.
# 10.   Print the final CrCl value using the str() function.

# 1. Prompt the user to enter age, weight, cr, and gender
# Using float for weight and Cr as they can be decimals, int for age
age = int(input("Enter age (years): "))
weight = float(input("Enter weight (kg): "))
Cr = float(input("Enter Cr (µmol/l): "))
gender = input("Enter gender (male/female): ").strip().lower()

# 2. Validate input values separately to report WHICH value needs correction
is_valid = True

if age >= 100:
    print("Error: Age input needs to be corrected (must be < 100).")
    is_valid = False

if not (20 < weight < 80):
    print("Error: Weight input needs to be corrected (must be > 20 and < 80).")
    is_valid = False

if not (0 < Cr < 100):
    print("Error: Cr input needs to be corrected (must be > 0 and < 100).")
    is_valid = False

if gender not in ["male", "female"]:
    print("Error: Gender input needs to be corrected (must be 'male' or 'female').")
    is_valid = False

# 3. Calculate CrCl ONLY IF all inputs are valid
if is_valid:
    if gender == "male":
        CrCl = ((140 - age) * weight) / (72 * Cr)
    elif gender == "female":
        CrCl = (((140 - age) * weight) / (72 * Cr)) * 0.85
        
    # Output the result, using str() as suggested in the PDF
    print("CrCl = " + str(CrCl))
# Pseudocode
# Creatine Clearance Calculator (Cockcroft-Gault Equation)
# 1. Input age, weight, gender, Cr
# 2. Validate inputs:
#     age < 100
#     weight > 20 AND weight < 80
#     Cr > 0 AND Cr < 100
#     gender is 'male' or 'female'
# 3. IF any input is invalid:
#     PRINT which value must be corrected
# 4.if gender=="male":
#   CrCl=(140-y)*w/(72*Cr)
#  elif gender=="female":
#  CrCl=(140-y)*w/(72*Cr)*0.85
#  else:  #the gender is invalid
#    print("error")
#  exit()  to stop the program immediately
#  prompt the user to enter age, weight, cr, and gender
y=int(input("age="))
w=int(input("weight="))
Cr=int(input("Cr="))
gender=input("gender(male/female)")

#calculate CrCl based on grnder 
if gender=="male":
    CrCl=(140-y)*w/(72*Cr)
elif gender=="female":
    CrCl=(140-y)*w/(72*Cr)*0.85
else:  #the gender is invalid
    print("error")
    exit() #stop the program immediately

#validate input values 
if y<100 and 20<w<80 and 0<Cr<100:
    print("CrCl=",CrCl)
else:
    print("input variable needs	corrected")
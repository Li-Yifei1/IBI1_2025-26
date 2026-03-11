#prompt the user to enter age, weight, cr, and gender
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
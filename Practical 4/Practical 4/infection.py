# Pseudocode
# Simulate daily infection spread
# 1. Set total_students = 91
# 2. Set initial_infected = 5
# 3. Set daily_growth_rate = 0.4
# 4. Set day_counter = 0
# 5. current_infected = initial_infected
# 6. WHILE current_infected < total_student
#    the loop continue until the total infected number get to 91
# 7. PRINT total days needed to infect all students

a=5 
#days of infection since start
d=1 
while a<91:   #the number of total students is 91, once the infected person get 91 or more, the loop stop 
    a=a*1.4 #the number of infected students the growth rate is 40%
    d=d+1   
    print(d,a) #print current day and its number of infected person
print ("all the students are infected after",d,"days") #print final result

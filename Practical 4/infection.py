#initial infector
a=5 
#days of infection since start
d=1 
while a<91:   #the number of total students is 91, once the infected person get 91 or more, the loop stop 
    a=a*1.4 #the number of infected students the growth rate is 40%
    d=d+1   
    print(d,a) #print current day and its number of infected person
print ("all the students are infected after",d,"days") #print final result

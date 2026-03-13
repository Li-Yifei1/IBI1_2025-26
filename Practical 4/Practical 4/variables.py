a=5.08 #population of 2004
b=5.33 #population of 2014
c=5.55 #population of 2024
d=b-a
e=c-b
print(d,"and",e)
if d<e:
    print("accelerating")
elif d>e:
    print("decelerating")
else:
    print("same")
# Answer: d=0.25 e=0.22
# d>e conclusion: decelerating

#store	Boolean	variables
X=True  #Init the variables
Y=False
W=X or Y
print(W)   #the answer is "True"

#| X | Y | W |
#|True|True|True|
#|True|False|True|
#|False|True|True|
#|False|False|False|
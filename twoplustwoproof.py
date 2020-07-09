#Defines two sets each with two elements
a = ['b', 'c']
d = ['e', 'f']
#Creates a union of a, b within set a
for let in d:
    a += let
#Prints length of set a, equivalent to the union of a, b
print (len(a))

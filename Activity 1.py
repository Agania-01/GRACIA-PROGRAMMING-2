def element(t):
    if len(t) < 3:
        return "The tuple is too short."
    return t[2]

#Calling the function
print(element((1, 2, 3, 4, 5)))  # this will print 3
print(element((1, 2)))           # While this will print "The tuple is too short." since the value inside is less than 3

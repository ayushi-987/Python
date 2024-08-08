'''
Type conversion can be handled in two manners:-
Type Convertion (Automatic)
Type Casting (Manually)
'''
 
 #In any arthematic operation between integer and float, It results in a float value.

# a=5
# b=9.045
# c=a+b
# print(c)

#We can't convert the string to float implicitly so we do type casting.
#Type casting doesn't work in case of string or charachter convertion to integer or float. 
#It only works if one data type can fit-in in another data type.

a=int("5")
b=8.75
c=a*b
print(c)
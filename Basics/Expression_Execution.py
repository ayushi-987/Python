#Operators in python can be read by https://www.scholarhat.com/tutorial/python/operators-of-python.
#String & numerics values can be operate together with *(repeat)

A,B=2,3
txt="@"
print(A*txt*B)

#String & string values can be operated together with +(concatenation)

C,D= "#",4
txt2="@"
print((C+txt2)*D)

#Numeric values can be operate with any arthematic operator
#Integer & Float can be operated & result in the 

E,F=2.5,2
print(E*F)

#The division of two integers always results in float

G,H=4,2
print(G/H)

#The integer Division convert the final result to integer type as it seems to be the rounded float number.
#Result of (A//B) is same as floor(A/B)

I,J=6,3
M=I//J
print(M)
print(type(M))

i,j=1.5,3
m=i//j
print(m)
print(type(m))

'''
Result of the reminder is negative only if denominator is negative.
num= + - - +
den= + - + -
res= + + + -
only in last case the reminder become (-ve)

'''

print(2%8, -10%-5, -4%2, 5%-2)

'''
Tuples:-
Tuples is the built-in datatype that creates the immutable sequence of different data types.
tuple=(1,2,3,4,5)
Similar to the strings in python
For single value tuples we need to define the element with comma separation:-
tup=(3,) else it will be treated as simple integer
tup=(5.0,)  float 
tup=("ayu",)  string
'''

tup=(3,5,0,8,9,0)
print(type(tup))

#Tuples methods:-

print(tup.index(5))
print(tup.count(0))
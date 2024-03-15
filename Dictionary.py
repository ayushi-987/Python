'''
Dictionary:-
Dictionary is the key-value pairs in python.
It is unordered, mutable, & don't allow duplicate keys.
Any Key value datatype can contain any type of value datatype.
Tuples are immutable so it can be placed as the key in dictionary
'''

info={
    "name" : "ayushi",
    "cgpa" : 10,
    "marks" : [98,99,97,98,100]
}
print(info)
print(type(info))
print(info["name"])

'''
For accessing any value from dictionary, we can get it by using key at the place of index in List
info["name]
'''
#Nested Dictionary:- Storing the dictionary inside a dictionary is refers to the nested distionary.
#For Example:-

topper={
    "place" : "Mahoba",
    "Details" : info,
    "Contact" : "9140423919" 
}

print(topper)

#Access the relevent info from the nested dictionary by using two square brackets like:-

print(topper["Details"]["cgpa"])


#Methods in Dictionary:-

print(topper.keys())
print(topper.values())
print(topper.items())
print(topper.get(""))

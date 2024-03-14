'''
String:- String is the squence of charachters
Basic Operations of String:-
Concatenation
"hello" + "world"= "helloworld"
length of string
len(str)
'''

a="hello"
b="world"
c=a+b
print(c)
print(len(c))

#Escape characheters in strings:- \n,\t

str="Hello, I'm learning python. It's Easy and portable language close to human"
print(str)
str2="Hello, I'm learning python. \nIt's Easy and portable language close to human"
print(str2)
str3="Hello, I'm learning python. \tIt's Easy and portable language close to human"
print(str3)

'''
Indexing:- Indexing in string is by default start 0
str=hello
ind=01234
By indexing we can only access the charachter not string manipulation allowed.

Slicing:- Accessing the part of the string
str_name[start_ind:end_ind]
str[:] => str[0:len(str)]
In positive Slicing will include RHS index.

Negative Indexing in Slicing:-By default it will start with -1 in RHS
str= h  e  l  l  o
ind=-5 -4 -3 -2 -1
Slicing will be => str[-4:-1]
In Negative slicing will include LHS index.
'''

paa= "JaynarayanSoni"
slic=paa[3:10]
print(slic)

#Strings Functions:-

Str="I am a Coder"
print(Str.endswith("er"))
print(Str.count("am"))
print(Str.replace("am", "are"))
print(Str.find("a"))
print(Str.capitalize())





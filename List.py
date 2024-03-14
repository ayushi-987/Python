'''
Lists in Python:- Same as Array in c++
Data type that stores the set of values.
Lists can store the value of different Data Types (integer, string, float etc)
'''

marks=[98,79,87,66,94]
student=["ayushi",2,98]
print(marks,student)
print(len(marks))

'''
Strings are immutable in Python whereas List is mutable in python.
As String slicing List slicing is also possible.
'''

#List Methods:-

lis = [4,9,7,3]
lis.append(2)
lis.sort()
lis.sort(reverse=True)
lis.reverse()
lis.insert(2,6)
lis.remove(7)
lis.pop(3)
print(lis)


#WAP to ask the user 3 fav movies and store them in a list
movie1=input("Write 1 fav movie:- ")
movie2=input("Write 2 fav movie:- ")
movie3=input("Write 3 fav movie:- ")
Li=[movie1,movie2,movie3]
print(Li)

#WAP to check whether the list is the palindromic list or not
#examples are:- [0,1,2,1,0] or [1,"abc","abc",1]

LI=[0,"abc","abc",0]
print(list(reversed(LI)))
if(LI==(list(reversed(LI)))):
    print("YES")
else:
    print("NO")


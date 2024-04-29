'''
Python can be used to perform some operations on the file(read or write)\
Types of Files:-
Text File:- .txt, .docx, .log, etc.
Binary File:- .mp4, .mov, .png, etc.

Existing Functions of file in python
open("File_name","mode") modes can be r/w default is read.

Read function in File return the file as the string 
'''

f=open("FILE.txt","r")
print(f.read())
print(type(f.read()))
f.close()

'''
Mode to open the file in python

"r":- read
"w":- write(overwrite)
"x":- create & open file in write mode
"a":- appending the file
"b":- binary file(need to add explicitly) 
"t":- text file(by default)
"+":- update the disk file in read and write format
we can combine 2-3 mode simultaneously

read function can specify the number of charachters you wanna read at a time
like f.read(5) initial 5 charachter will be read by this

for reading an entire file at once use :- f.read()
if want to read the file line by line use:- f.readline()

'''

f=open("FILE.txt","r")
while True:
    q=print(f.readline())
    if not q:
        break
'''
Sets:- Collections of the unordered data items that are immutable and unique.
Tuples can be stored on the sets but list,dictionary cannot be stored in set.
'''

nums = {1,2,2,2,3,4}
print(type(nums))
print(nums) #same values are printed single times so the duplicate values can be ignored.

print(len(nums)) #actual length of nums is 6 but duplicate values are counted 1 time.

num={}
print(type(nums)) # it refers the empty dictionary and not the empty set.

nu=set() #it is the empty set 

#Set Methods:-

nums.add(6)
print(nums)
nums.remove(3)
print(nums)
nums.pop()
print(nums)
nums.clear()
print(nums)

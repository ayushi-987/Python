# website used:- regexr.com
#https://devopslearning.medium.com/python-regular-expression-8ee28d35f3a7

'''

\w : sequence of word-like characters [a-zA-Z0–9_] that are not space
\d: Any numeric digit[0–9]
\s: whitespace characters(space,newline,tab)
\D: match characters that are NOT numeric digits
\W: match characters that are NOT words,digit or underscore
\S: match characters that are NOT spaces,tab or newline
+ : 1 or more
* : 0 or more
?: 0 or 1
{k}: exactly integer K occurence
{m,n}: m to n occurence inclusive
. :matches any character except the newline(\n)
^: start of the string
$: end of string
\: escape character 

'''

import re

# Compile a regex pattern
pattern = re.compile(r'\d+')

# Search for the pattern in a string
search_result = pattern.search('The house number is 1234')
if search_result:
    print("Search result:", search_result.group())  # Output: 1234

# Match the pattern at the beginning of a string
match_result = pattern.match('1234 is the house number')
if match_result:
    print("Match result:", match_result.group())  # Output: 1234

# Find all matches of the pattern in a string
findall_result = pattern.findall('House numbers: 1234, 5678, and 91011')
print("Findall result:", findall_result)  # Output: ['1234', '5678', '91011']

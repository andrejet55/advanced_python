'''You are given a 0-indexed binary string s having an even length.

A string is beautiful if it's possible to partition it into one or more substrings such that:

Each substring has an even length.
Each substring contains only 1's or only 0's.
You can change any character in s to 0 or 1.

Return the minimum number of changes required to make the string s beautiful.

Example 1:

Input: s = "1001"
Output: 2
Explanation: We change s[1] to 1 and s[3] to 0 to get string "1100".
It can be seen that the string "1100" is beautiful because we can partition it into "11|00".
It can be proven that 2 is the minimum number of changes needed to make the string beautiful.
Example 2:

Input: s = "10"
Output: 1
Explanation: We change s[1] to 1 to get string "11".
It can be seen that the string "11" is beautiful because we can partition it into "11".
It can be proven that 1 is the minimum number of changes needed to make the string beautiful.
Example 3:

Input: s = "0000"
Output: 0
Explanation: We don't need to make any changes as the string "0000" is beautiful already.
'''

import re


def find_beautiful(s: str):
    # Make sure that s length is even
    if len(s) % 2 != 0:
        print("String is not beautiful. Substrings can't have an even length\n-------------------------")
        return

    # counts the numbers that needs to be changed
    changes = 0
    # saves the new string
    new_s = ""

    # iterate through pairs
    for i in range(0, len(s), 2):
        # compare the current digit with the next one
        if s[i] != s[i+1]:
            changes += 1
        new_s += s[i] * 2

    # change
    print(f"S= {s}\nNumber of changes: {changes}. Final string: {new_s}\n-------------------------")


find_beautiful("1001")
find_beautiful("101")
find_beautiful("0000")

'''
---------
Write a Python program to find all the numbers from 0-9 from a string:

input: '89ADFRE41'

Output :[8941]
'''
# From scratch


def find_numbers(input: str):
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    result = []
    for s in input:
        if s in digits:
            result.append(s)

    whole_number = ''

    for d in result:
        whole_number += d

    print([int(whole_number)])


find_numbers('89ADFRE41')


# Using regex
def find_numbers_re(input: str):
    result = re.findall('[0-9]', input)

    whole_number = ''

    for d in result:
        whole_number += d

    print([int(whole_number)])


find_numbers_re('89ADFRE41')

'''
----------

Write a Python program to find two elements once in a list where every element appears exactly n times in the list. 
Input : [1, 2, 1, 3, 2, 5], 2    (n=2)
Output :[5, 3]

'''


'''

-----------

 Write a Python program to reverse the digits of an integer. 
Input : 234
Input : -234
Output: 432
Output : -432

-------

'''


'''

You are given three integers start, finish, and limit. You are also given a 0-indexed string s representing a positive integer.

A positive integer x is called powerful if it ends with s (in other words, s is a suffix of x) and each digit in x is at most limit.

Return the total number of powerful integers in the range [start..finish].

A string x is a suffix of a string y if and only if x is a substring of y that starts from some index (including 0) in y and extends to the index y.length - 1. For example, 25 is a suffix of 5125 whereas 512 is not.

 

Example 1:

Input: start = 1, finish = 6000, limit = 4, s = "124"
Output: 5
Explanation: The powerful integers in the range [1..6000] are 124, 1124, 2124, 3124, and, 4124. All these integers have each digit <= 4, and "124" as a suffix. Note that 5124 is not a powerful integer because the first digit is 5 which is greater than 4.
It can be shown that there are only 5 powerful integers in this range.
Example 2:

Input: start = 15, finish = 215, limit = 6, s = "10"
Output: 2
Explanation: The powerful integers in the range [15..215] are 110 and 210. All these integers have each digit <= 6, and "10" as a suffix.
It can be shown that there are only 2 powerful integers in this range.'''

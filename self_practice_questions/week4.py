# First one
'''Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
'''

def patterns(s:str, p:str)-> bool:
    """_summary_
    Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' w

    Args:
        s (str): _description_
        p (str): _description_

    Returns:
        bool: _description_
    """
    
    # Initialize a table to save the string and pattern characters
    ''' We initialize a 2D dynamic table with len(s) + 1 rows and len(p) + 1 columns.
    This table will store whether a substring of s (up to length i) matches a sub-pattern of p (up to length j).
    The table is initialized with False as we want to assume that no substrings or sub-patterns match at the beginning.
    The extra +1 for both s and p is in case that both the string and pattern could be empty.'''
    table = []
    for x in range(len(s) + 1):
        table.append([False] * (len(p) + 1))
                 
    # Base case empty string (s = "") matches an empty pattern (p = "")
    table[0][0] = True
    
    # Handles the case where the pattern starts with something like a*, b*, or even .*. 
    # These patterns can match zero characters, so we want to initialize the table to reflect that.
    for j in range(2, len(p) + 1):
        if p[j - 1] == '*':
            table[0][j] = table[0][j - 2]
    
    # iterate through each character of the string s and pattern p
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            # checks whether the current characters from the string and pattern match
            if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                table[i][j] = table[i - 1][j - 1]
            # Handles the case where the pattern character is a *
            elif p[j - 1] == '*':
                table[i][j] = table[i][j - 2]  # Zero occurrence case
                # handles the one or more occurrences case for *
                if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                    table[i][j] = table[i][j] or table[i - 1][j]  # One or more occurrence case
    
    # checks whether the entire string s matches the entire pattern p
    # If dp[len(s)][len(p)] is True, it means that the pattern p matches the entire string s, so we return True.
    # Otherwise, we return False.
    return table[len(s)][len(p)]


patterns(s="aa",p="a")

# SECOND ONE

'''
----------------------
You are given a 0-indexed integer array nums having length n, an integer indexDifference, and an integer valueDifference.

Your task is to find two indices i and j, both in the range [0, n - 1], that satisfy the following conditions:

abs(i - j) >= indexDifference, and
abs(nums[i] - nums[j]) >= valueDifference
Return an integer array answer, where answer = [i, j] if there are two such indices, and answer = [-1, -1] otherwise. If there are multiple choices for the two indices, return any of them.

Note: i and j may be equal.

Example 1:

Input: nums = [5,1,4,1], indexDifference = 2, valueDifference = 4
Output: [0,3]
Explanation: In this example, i = 0 and j = 3 can be selected.
abs(0 - 3) >= 2 and abs(nums[0] - nums[3]) >= 4.
Hence, a valid answer is [0,3].
[3,0] is also a valid answer.

Example 2:

Input: nums = [2,1], indexDifference = 0, valueDifference = 0
Output: [0,0]
Explanation: In this example, i = 0 and j = 0 can be selected.
abs(0 - 0) >= 0 and abs(nums[0] - nums[0]) >= 0.
Hence, a valid answer is [0,0].
Other valid answers are [0,1], [1,0], and [1,1].

Example 3:

Input: nums = [1,2,3], indexDifference = 2, valueDifference = 4
Output: [-1,-1]
Explanation: In this example, it can be shown that it is impossible to find two indices that satisfy both conditions.
Hence, [-1,-1] is returned.'''

# Third ONe

"""------------------------
Write a Python program to find the single element in a list where every element appears multiple times except for one.
Input : [5, 3, 4, 3, 5, 5, 3],
Output : 4

 

Write a Python program to compute and return the square root of a given 'integer'. 
Input : 16
Output : 4
Note : The returned value will be an 'integer', do not use square root functions from python.

 

Write a Python program to check a sequence of numbers is a geometric progression or not. 
Input : [2, 6, 18, 54]
Output : True"""



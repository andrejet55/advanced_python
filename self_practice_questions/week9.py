
# ANDREA FRANCO C0931897


'''Q1: A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers. Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"

Output: true

Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"

Output: false

Explanation: "raceacar" is not a palindrome.'''

import re
s = "A man, a plan, a@ &c/anal: Panama"


def palindrome(s):
    # convert to lowercase
    s = s[0].lower() + s[1:].lower()
    print(s)

    # remove alphanumeric
    clean_word = re.findall(pattern="[a-zA-Z]", string=s)

    num = len(clean_word)//2
    # compare the letters from the beggining and end
    for i in range(num):
        if clean_word[i] != clean_word[-i-1]:
            return False

    return True


print(palindrome(s))


"""Q2 Given an array nums of size n, return the majority element. The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]

Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]

Output: 2"""


def majority_element(nums):
    count_dict = {}
    majority = 0
    majority_number = 0

    for num in nums:
        if num not in count_dict:
            count_dict[num] = 1
        else:
            count_dict[num] += 1

    for num, count in count_dict.items():
        if count > majority:
            majority = count
            majority_number = num
    return majority_number


nums = [3, 2, 3]
print(majority_element(nums))

nums = [2, 2, 1, 1, 1, 2, 2]
print(majority_element(nums))

"""Q3 Write an algorithm to determine if a number n is happy. A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

 Example 1:

Input: n = 19

Output: true

Explanation:

12 + 92 = 82

82 + 22 = 68

62 + 82 = 100

12 + 02 + 02 = 1

Example 2:

Input: n = 2

Output: false"""


def is_happy(n):
    # sum of squares
    sum_of_sq = 0
    while sum_of_sq != 1:

        for i in n:
            sum_of_sq += i**2
            pass

    return True

# n = 2
# print(is_happy(n))


n = 19
print(is_happy(n))


"""Q4. 
You are given an integer array nums. We call a subset of nums good if its product can be represented as a product of one or more distinct prime numbers.

For example, if nums = [1, 2, 3, 4]:
[2, 3], [1, 2, 3], and [1, 3] are good subsets with products 6 = 2*3, 6 = 2*3, and 3 = 3 respectively.
[1, 4] and [4] are not good subsets with products 4 = 2*2 and 4 = 2*2 respectively.
Return the number of different good subsets in nums modulo 109 + 7.

A subset of nums is any array that can be obtained by deleting some (possibly none or all) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.

 

Example 1:

Input: nums = [1,2,3,4]
Output: 6
Explanation: The good subsets are:
- [1,2]: product is 2, which is the product of distinct prime 2.
- [1,2,3]: product is 6, which is the product of distinct primes 2 and 3.
- [1,3]: product is 3, which is the product of distinct prime 3.
- [2]: product is 2, which is the product of distinct prime 2.
- [2,3]: product is 6, which is the product of distinct primes 2 and 3.
- [3]: product is 3, which is the product of distinct prime 3.
Example 2:

Input: nums = [4,2,3,15]
Output: 5
Explanation: The good subsets are:
- [2]: product is 2, which is the product of distinct prime 2.
- [2,3]: product is 6, which is the product of distinct primes 2 and 3.
- [2,15]: product is 30, which is the product of distinct primes 2, 3, and 5.
- [3]: product is 3, which is the product of distinct prime 3.
- [15]: product is 15, which is the product of distinct primes 3 and 5."""

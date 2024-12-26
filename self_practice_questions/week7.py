"""Q1 )

Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not."""


def is_palindrome(x: int):
    # convert to string
    x = str(x)

    # save the digits of x
    split_x = []
    for digit in x:
        split_x.append(digit)

    result = True

    for i in range(len(x)//2):
        print(f"left: {split_x[i]} right: {split_x[-i-1]}")
        if split_x[i] != split_x[-i-1]:
            result = False

    print(f"Output: {result}\n-------------")


print(f"-----------Palindrome test:------------------")

number = 12321
print(f"input number: {number}")
is_palindrome(number)

number = 123214
print(f"input number: {number}")
is_palindrome(number)


"""Q2)

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value

I             1

V             5

X             10

L             50

C             100

D             500

M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"

Output: 3

Explanation: III = 3.

 

Input: s = "LVIII"

Output: 58

Explanation: L = 50, V= 5, III = 3."""
print(f"-----------Roman to Numbers test:------------------")


def roman_numerals(s: str):
    # First create equivalences:
    roman2dec = {"I": 1,
                 "V": 5,
                 "X": 10,
                 "L": 50,
                 "C": 100,
                 "D": 500,
                 "M": 1000}

    # store the result
    result = 0
    previous_value = 0
    value = 0

    reversed_s = reversed(s)

    for digit in reversed_s:

        value = roman2dec[digit]

        if value < previous_value:
            result -= value
        else:
            result += value

        previous_value = value

    print(f"Output: {result}\n--------------")


s = "III"
print(f"Input: {s}")
roman_numerals(s)

s = "LVIII"
print(f"Input: {s}")
roman_numerals(s)

s = "CMXLVIII"
print(f"Input: {s}")
roman_numerals(s)


"""Q3
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []"""


def linked_lists(lists: list):

    numbers = []
    for list in lists:
        for digit in list:
            numbers.append(digit)

    numbers.sort()

    print(f"Output: {numbers}\n-----------")


print("------------Q3 - LINKED LIST ----------------")

lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
print(f"input: {lists}")
linked_lists(lists)

lists = []
print(f"input: {lists}")
linked_lists(lists)

lists = [[]]
print(f"input: {lists}")
linked_lists(lists)

'''
Andrea Franco (c0931897)

'''

import pandas as pd

#1

def four_numbers_sum(numbers:list, target_n:int) -> list:
    '''program to find 4 numbers from an array such that the sum of 4 numbers equal to a given number.'''
    # variable to save the groups of numbers
    output = []
    
    # get the different pair combinations of numbers
    combination = {}
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if (numbers[i]+numbers[j]) in combination:
                combination[numbers[i]+numbers[j]].append([i,j])
            else:
                combination[numbers[i]+numbers[j]] = [[i,j]]

    # compare each combination sum with the goal
    for pair_sum, pairs in combination.items():
        
        second_pair_sum = target_n - pair_sum
        
        if second_pair_sum in combination:
            for pair1 in pairs:
                for pair2 in combination[second_pair_sum]:
                    # Make sure that all indices are unique
                    if len(set(pair1 + pair2)) == 4:
                        result = sorted([numbers[pair1[0]], numbers[pair1[1]], numbers[pair2[0]], numbers[pair2[1]]])
                        if result not in output:
                            output.append(result)
       
    return output

numbers = [1, 0, -1, 0, -2, 2, 10, 11]
target_n = 0
print(four_numbers_sum(numbers, target_n))




#2
def single_element(numbers:list) ->int:
    '''program to add the digits of a positive integer repeatedly until the result has a single digit.'''
    # count number of occurrences of each value
    counts = pd.Series(numbers).value_counts()

    # single value
    single = 0

    # assign the single value
    for i in counts.index:
        if counts[i] == 1:
            single = i
        else:
            continue

    # manually:
    #counts = {}
    # for i in range(len(numbers)):
        #if i not in numbers:
        #   counts[numbers[i]] = 1
        #else:
        #   counts[numbers[i]] += 1

    # assign single value
    #for key, value in counts.items():
    #    if value == 1:
    #        single = key
    #    else:
    #        continue

    return single

print(single_element([1, 1, 1, 2, 2, 2, 3]))

def add_digits(number:int) -> None:
    '''program to add the digits of a positive integer repeatedly until the result has a single digit'''
    
    # keep running until result < 2 digits
    while number >= 10:
        # convert to a string
        digits = str(number)
        
        number = 0
        
        # slice and sum
        for i in range(len(digits)):
            number += int(digits[i])
            
    print(number)


add_digits(48)
add_digits(59)
'''
Do not use any of Python functions:

A-Write a Python program to check if a number is a perfect square

B- Write a Python program to find a missing number from a list. 
Input : [1,2,3,4,6,7,8]
Output : 5

 

C- Write a Python program to find the single number in a list that doesn't occur twice.
Input : [5, 3, 4, 3, 4]
Output : 5
'''

#A
def check_square() -> None:
    '''
    Check if a given number is a perfect square'''
    
    # user input
    number = int(input("Enter the number\n"))
    root = number**0.5
    
    # if the number is a perfect square, its square root should be an integer.
    print("Is the number a perfect square?", (int(root) == root))

#check_square()

#B
def find_missing_number(numbers) -> None:
    '''Python program to find a missing number from a list. '''
    
    for i in range(len(numbers)):
        if numbers[i] != i+1:
            print("Missing number is", i+1)
            break
        else:
            continue


find_missing_number([1,2,3,4,6,7,8])


#C
def single_number(numbers) -> None:
    '''Python program to find the single number in a list that doesn't occur twice.'''
    
    count = {}
    for i in range(len(numbers)):
        if numbers[i] not in count.keys():
            count[numbers[i]] = 1
        else:
            count[numbers[i]] += 1 
    
    for key, value in count.items():
        if value == 1:
            print(f'The single number is: {key}')

single_number([5, 3, 4, 3, 4])

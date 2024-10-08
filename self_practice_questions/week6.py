'''1-Write a Python program to check a sequence of numbers is an arithmetic progression or not. 
Input : [5, 7, 9, 11]
Output : True
In mathematics, an arithmetic progression or arithmetic sequence is a sequence of numbers such that the difference between the consecutive terms is constant.
For example, the sequence 5, 7, 9, 11, 13, 15 ... is an arithmetic progression with common difference of 2.'''

def check_ari_seq(n:list):
	# save the difference between the first pair of numbers. As it is a constant we don't need to update it.'
	dif = 0
	# save the result of the check
	result = False

	# iterate through the list
	for i in range(len(n)-1):
		if i == 0:
			dif = n[i] - n[i+1]
		else:
			# if the pattern changes, return false
			if (n[i] - n[i+1]) != dif:
				return False
			else:
				result = True
	return result
 
sequence = [5,7,9,11,13,15]
sequence2 = [5,7,9,10,13,15]

print("Sequence", sequence, "is an arithmetic sequence:", check_ari_seq(sequence))
print("Sequence",sequence2, "is an arithmetic sequence:", check_ari_seq(sequence2))
 
 
'''
2-Write a Python program to check whether a given number is an ugly number. 
Input : 12
Output : True
Ugly numbers are positive numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, ...
shows the first 10 ugly numbers.
Note: 1 is typically treated as an ugly number
'''
 
def ugly_numbers(n:int):
	# ugly prime factors
	ugly_pf = [2,3,5]

	# obtain prime factors of the number
	prime_factors = []
	i = 2
	while n != 1:

		if n%i == 0:
			prime_factors.append(i)
			n = n/i
			
		else:
			i +=1
 
	# seek for other numbers rather than 2,3,5
	for number in prime_factors:
		if number not in ugly_pf:
			return False
	return True
	
		

ugly_number = 12
not_ugly = 7
print(ugly_number,"is an ugly number?:", ugly_numbers(ugly_number))
print(not_ugly, "is an ugly number?:", ugly_numbers(not_ugly))

'''
3-Write a Python Function to find the single number in a list that doesn't occur n times.
Input : [5, 3, 3, 4, 4, 3, 4], N=3
Output : 5
'''

def find_single_number(sequence: list, n: int):
	# save the count of each number
	counts = {}
	
	for number in sequence:
		if number not in counts:
			counts[number] = 1
		else:
			counts[number] += 1
	
	for key, value in counts.items():
		if value != n: 
		    return key
  


seq = [5,3,3,4,4,3,4]
n = 3
print("Single number in the sequence:",seq, "is: ", find_single_number(seq, n))
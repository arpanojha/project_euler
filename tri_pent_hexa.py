numbers = []
import csv
import math
def main():
    n = hexagonal_numbers(numbers)
    #print(min_D_pair(n))
    #print(check_triangle(40756))
    #print(check_pentagon(40756))
    print(min_D_pair(n))

def min_D_pair(n):    # like mindy pair(friends sitcom)
	for i in n:
		if i ==1:
			continue
		k = 0
		k = check_pentagon(i)+check_triangle(i)
		if k == 2:
			if i == 40755:
				continue
			else:
			    return i 
	return 0

# \b^2 - 2.a.c
# a = 1 b = 1, c = -k
def check_integer(k):
	if math.ceil(k)==math.floor(k):
		return 1
	return 0

def check_pentagon(a):    
	k = 2*a
	n = math.sqrt(1+(4*k))
	n = (n-1)/2
	return check_integer(n)

def check_triangle(a):
    k = 2*a
    n = math.sqrt(1+(12*k))
    n = (n+1)/6
    return check_integer(n)

def pentagonal_numbers(numbers):
	for i in range(1,500):
		n = int((i*((3*i)-1))/2)
		numbers.append(n)
	print(numbers)
	return numbers

def triangle_numbers(numbers):
	for i in range(1,100):
		n = int((i*(i+1))/2)
		numbers.append(n)
	print(numbers)
	return numbers

def hexagonal_numbers(numbers):
	for i in range(1,100000):
		n = i*((2*i)-1)
		numbers.append(n)
	print(numbers)
	return numbers

if __name__ == '__main__':
	main()
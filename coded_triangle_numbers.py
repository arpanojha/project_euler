numbers = []
import csv
def main():
    n = triangle_numbers(numbers)
    print(count_of_codes(n))

def count_of_codes(n):
	k = read_file_xlx()
	sum1 = 0
	for m in k:
		sum1 = sum1 + check_length(m,n)  
	return sum1

def check_length(a,n):    #match the length of each word
	m = len(a)
	#print(m)
	if m in n:
		return 1
	else:
		return 0


def read_file_xlx():     #read the text file
    with open('triangle.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            k = row
    return k


def triangle_numbers(numbers):
	for i in range(1,100):
		n = int((i*(i+1))/2)
		numbers.append(n)
	return numbers

if __name__ == '__main__':
	main()
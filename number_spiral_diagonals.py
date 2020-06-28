data = [1]*4
def main():
	print(value_of_spirals(501))
	m,n = check_size(101)
	print(m-n+1)

# 9-5  7-4  5-3   3-2
def value_of_spirals(n,sum1=1,k=2):
	if n == 1:
		return sum1
	for i in range(0,4):
		data[i] = data[i] + k
		k=k+2
		sum1 = sum1 + data[i]
	return value_of_spirals(n-1,sum1,k)



'''
1  +2  3  +10  13  +18   31
1  +4  5  +12  17  +20   37
1  +6  7  +14  21  +22   43
1  +8  9  +16  25  +24   49
'''
j = 1
l = 0
sum1 = 1
def check_size(n, j = 1, l = 1,m=2,sum1=0):
	if n == 1:
		return sum1,l
	if j == 5:
		n=n-2
		j = 1
		m= m+2
	
	l = l + m
	sum1 = sum1 + l
	#print(l, sum1)
	j = j + 1
	return check_size(n,j,l,m,sum1)

if __name__ == "__main__":
	main()
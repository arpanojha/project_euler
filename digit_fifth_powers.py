
def main():
	print(digit_fifth_powers(1000))
	#print(check_cond(8301))

def digit_fifth_powers(seed):
	val = 0
	i = seed-1
	while(i<100000):
		i=i+1
		if i == check_cond(i):
			print(i)
			val = val+i


	return val

def check_cond(num,sum1 = 0):
	if num == 0:
		return int(sum1)
	j = int(num%10)
	sum1 = sum1 + pow(j,5)
	num = int(num/10)
	return check_cond(num,sum1)
 

if __name__ == "__main__":
	main()


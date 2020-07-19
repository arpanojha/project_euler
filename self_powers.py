import math
def main():
	k = self_powers_brute_force()
	m = k%10000000000
	print(m)

def self_powers_brute_force():
	sum1 = 0
	for i in range(1,1000):
		sum1 = sum1 + pow(i,i)
	return sum1

if __name__ == '__main__':
	main()
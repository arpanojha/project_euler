num = []
k = []
def main():
	print(prime_permutations())
	#print(k)
	print(len(k))

def prime_permutations():
	for i in range(1001,10000,2):
		l = check_prime(i)
		if(l==0):
			continue
	i=0
	for i in range(len(k)-1):
		#print(i,len(k))
		for j in range(i+1,len(k)):
			verd = check_permutation(k[i],k[j])
			if verd == 0:
				continue
			diff = k[j]-k[i]
			#print(k[i],k[j],k[j]+diff)
			if k[j]+diff not in k:
				continue

			verd = check_permutation(k[j],k[j]+diff)
			if verd ==0:
				continue
			s = str(k[i])+str(k[j])+str(k[j]+diff)
			num.append(s)
	return num
def check_permutation(a,b):
	m=[int(x) for x in str(a)]
	n=[int(x) for x in str(b)]
	m.sort()
	n.sort()
	if m == n:
		return 1
	return 0

def check_prime(a):
	for i in range(3,int(a/2)+1,2):
		if a%i ==0:
			return 0
	k.append(a)
	return 1



if __name__ == '__main__':
	main()
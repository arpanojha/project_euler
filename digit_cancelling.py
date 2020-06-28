
def main():
	print(digit_cancelling_fractions(1000))


def digit_cancelling_fractions(seed):
	k=1
	for i in range(11,100):
		if i%10 == 0:
			pass	
		for j in range(10,i):
			v,p = common_cancel(i,j)
			if v == -1:
				pass
			if p is not 0:
			    if j/i == v/p:
			    	if j%10 is not 0:
				        print(i,j)
				        k = k*j





	return k

def common_cancel(i,j):
    o = j%10
    p = int(j/10)
    m = i%10
    n = int(i/10)
    if o == m:
    	return p,n
    if p == n:
    	return o,m
    if o == n:
    	return p,m
    if p == m:
    	return o,n
    return -1,-1

if __name__ == "__main__":
	main()


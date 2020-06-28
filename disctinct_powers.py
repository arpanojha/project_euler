
l =99*99
x = [0]*l
def main():
	print(count_distinct())

def count_distinct():
	m = 0
	for i in range(2,6):
		for j in range(2,6):
			val = pow(j,i)
			if val not in x:
				x[m]=val
				m=m+1



	return m
 

if __name__ == "__main__":
	main()


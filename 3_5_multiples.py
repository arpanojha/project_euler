

def main():
    a = find_multiples(1000,3)
    b = find_multiples(1000,5)
    c = find_multiples(1000,15)
    print(a+b-c)

def arithmetic_progression(r,d,n):
    if n == 0 :
        return 0
    return (n/2)*((2*r)+(n-1)*d)
def find_multiples(num,k):
    n1 = find_number_multiples(num,k)
    n1 = arithmetic_progression(k,k,n1)

    return n1

def find_number_multiples(n,d):
    return int((n-1)/d)
if __name__ == '__main__':
    main()

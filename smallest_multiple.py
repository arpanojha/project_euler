
def main():
    print(find_multiple(11))

def find_multiple(n):
    p=n
    while(n>0):
        if (p%n) is not 0:
            val = gcd(p,n)
            p=int((p*n)/val)
        n=n-1
    return p
def gcd(a,b):
    gcd_val = 1
    i=1
    if a == b:
        return a
    while(i<=b):
        if a%i == 0:
            if b%i ==0:
                gcd_val = i
        i=i+1
    return gcd_val
if __name__ == '__main__':
    main()

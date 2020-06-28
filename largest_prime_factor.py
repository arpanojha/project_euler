

def main():
    print(find_largest_prime(13195))
    #print(gcd(13195))
def find_largest_prime(n):
    largest_prime = 1
    i=1
    while(i<int(n/2)):
        if n%i == 0:
            val = gcd(n,i)
            if gcd(val,int(val/2)) == 1:
                largest_prime = i
        i=i+1
    return largest_prime

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
    return int(gcd_val)

if __name__ == '__main__':
    main()

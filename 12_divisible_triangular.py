
def main():
    m = find_divisible_triangle(6)
    #print(m)
    j = 1000
    while(1):
        m = find_divisible_triangle(j)
        k = find_over_divisors(m)
        print(k)
        if k >500:
            print("500 div crossed at :",j," num div: ",k)
            break
        j+=1
    #print(find_over_divisors(int(m)))

def find_divisible_triangle(n):
    s = (n/2)*(n+1)
    return s
def find_over_divisors(n):
    count = 0
    k=1
    while(k<(int((n/2))+1)):
        if n%k == 0:
            #print(k)
            count = count+1
        k=k+1
    return count+1
if __name__ == '__main__':
    main()

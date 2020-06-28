m = [0]*100002
s1 = 2000000

def main():
    m[0]=1
    m[1]=2
    m[2]=3
    print(largest_prime_iteration(4,1000))
# 0 means prime / 1 means not prime


def largest_prime_iteration(val,iter):
    j=3
    sum = 6
    while(j<(iter+1)):
        i=1
        flag =0
        if sum > s1:
            return sum-val
        for i in range(1,j):
            if val%m[i] == 0:
                flag = 1
                break
        if flag ==0:
            #print(val)
            sum += val
            m[j] = val
            j  =j+1
        val = val+1
    return sum-val

if __name__ == '__main__':
    main()

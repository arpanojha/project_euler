m = [0]*100002


def main():
    m[0]=1
    m[1]=2
    m[2]=3
    print(largest_prime_iteration(4,100001))
# 0 means prime / 1 means not prime
def largest_prime(val,j):
    if j == 1000:
        return m[j-1]
    i=1
    flag =0
    for i in range(1,j):
        if val%m[i] == 0:
            flag = 1
            break
    if flag ==0:
        #print(val)
        m[j] = val
        j=j+1
    val = val+1
    return largest_prime(val,j)

def largest_prime_iteration(val,iter):
    j=3
    while(j<(iter+1)):
        i=1
        flag =0
        for i in range(1,j):
            if val%m[i] == 0:
                flag = 1
                break
        if flag ==0:
            #print(val)
            m[j] = val
            j  =j+1
        val = val+1
    return m[j-1]

if __name__ == '__main__':
    main()

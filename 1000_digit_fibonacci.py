s = [0]*100000
s[1]=1
s[2]=1
s[3]=2
n=20
def main():
    m = str(find_fib_numbers(500))
    #print(len(m))
    find_length()

def find_1000_th():
    return 0
def find_fib_numbers(n):
    i = 4
    while(i<n+1):
        s[i] = s[i-1]+s[i-2]
        i=i+1
    return s[n]

def find_length():
    i=1
    count = 1
    m_prev = 0
    while(i<10000):
        count = count +1
        m = str(s[i])
        i=i+1
        c_prev = count
        if m_prev is not len(m):
            #print(count)
            count = 1
        if count ==1 :
            print(len(m),c_prev)
        m_prev = len(m)
        if s[i]==0:
            break
    return 0

if __name__ == '__main__':
    main()

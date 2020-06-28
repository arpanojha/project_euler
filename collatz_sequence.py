s = 1000000
def main():
    print(collatz_seq(s))

def collatz_seq(n):
    c = 1
    max = 1
    while(n>5):
        val = n
        i = check_length(n,1)
        #print(i)
        if i > max:
            max = i
            c = n
        n = n-1
    return max, c
def check_length(n,c):
    if n == 1:
        return c
    c=c+1
    if n%2 == 0:
        return check_length(even_movement(n),c)
    else:
        return check_length(odd_movement(n),c)
def even_movement(n):
    return int(n/2)

def odd_movement(n):
    return ((3*n)+1)

if __name__ == '__main__':
    main()

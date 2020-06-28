


def main():
    print(find_required())

def find_required():
    k = 0
    a = 1
    b = 1
    sum = 0
    n = 4000000
    while(k<n):
        k=return_fib(a,b)
        if k%2 == 0:
            sum += k
        a = b
        b = k
    return sum

def return_fib(m,n):
    return m+n


if __name__ == '__main__':
    main()

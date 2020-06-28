

def main():
    print(check(999,999))

def check(a1,b1,perc = 0.9):
    a=a1
    b=b1
    m = int(b*perc)
    if perc == 0.0:
        return "Nothing found"
    while(a>m):
        while(b>m):
            prod = a*b
            if check_palindrome(prod) == 1:
                return a,b
            b=b-1
        a=a-1
        b=999
    return check(a1,b1,perc-0.1)



def check_palindrome(a):
    a = str(a)
    b = a[::-1]
    if a == b:
        return 1
    return 0

if __name__ == '__main__':
    main()

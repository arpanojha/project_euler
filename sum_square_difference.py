
def main():
    print(find_sum_squares(100)-find_square_sum(100))

def find_square_sum(n):
    if n==1:
        return 1
    return n*n+find_square_sum(n-1)

def find_sum_squares(n):
    n = (n/2)*(n+1)
    return n*n

if __name__ == '__main__':
    main()

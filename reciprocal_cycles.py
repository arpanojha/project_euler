m = ([0]*1000)
m[0]=1
def main():
    find_reciprocal_cycle()
    k = 0
    for i in m:
        print(k,i)
        k=k+1
        if i == 0:
            break

def find_reciprocal_cycle():
    for d in range (1,100):
        m[d] = format(1/d, '.12g')
        d=d+1
    return d
def find_repetitive():
    for i in range(1,10):
        k = str(m[i])
        find_largest_repeating(k)
def find_largest_repeating():
    return 0

if __name__ == '__main__':
    main()

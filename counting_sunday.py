
def main():
    print(count_sundays())

def count_sundays():
    i = 1901
    j = 0
    sun = 0
    k = 1
    while(i<2000):
        while(j<12):
            if i%4 == 0:
                k = k+2
            k = k+1
            j=j+1
            if k%7 == 6:
                sun = sun+1
        i=i+1
        j=0
    return sun


if __name__ == '__main__':
    main()

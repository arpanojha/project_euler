s = 10
arr = [[1]*s]*s
count = 0
def main():
    print()
    print(find_lattice_paths(0,0))

#
def find_lattice_paths(i,j):
    if i == s or j == s:
        return 0
    if i == s-1 and j == s-1:
        return 1
    return find_lattice_paths(i+1,j) + find_lattice_paths(i,j+1)

if __name__ == '__main__':
    main()

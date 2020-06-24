import string
def print_rangoli(size):
    # your code goes here
    alp = list(string.ascii_lowercase)
    for i in range(size*size):
        print(str(alp[size].center(size**3
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

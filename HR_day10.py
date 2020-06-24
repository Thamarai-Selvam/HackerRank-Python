count = 0
def findone(n):
        return max(map(len, n[2:].split('0')))
N = int(input())
binary = bin(N)
count = findone(binary)
print(count)


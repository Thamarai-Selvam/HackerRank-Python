phoneBook ={}
key = list()
N = int(input())
for i in range(N):
    name = input('name')
    value = input('val')
    phoneBook[name] = value
for i in range(N):
    key.append(input()) 
print(key)
for i in range(N):
    print(key[i],'=',phoneBook[key[i]])

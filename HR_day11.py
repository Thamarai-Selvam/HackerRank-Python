arr = []
for i in range(6):
    arr.append(list(map(int, input().rstrip().split())))
hourglass = []
for i in range(3):
    for j in range(3):
        if(i == 1):
            if(j == 2): hourglass.append(list(map(int,arr)))
            else: hourglass.append(0)
            hourglass.append(list(map(int,arr)))
print(hourglass)

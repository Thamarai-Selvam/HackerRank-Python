s = list(map(int,input().split()))
cen = 3
for i in range(s[0]):
    for j in range(s[1]):
        if(j != int( s[1] / 2 - cen)):            
            print('-',end='')
            cen = cen + 1
        else:
            print('.|.',end='')
    print('\n')
        

T = int(input())
for i in range(T):
    N = int(input())
    tmp = N
    count = 0
    while(tmp > 0):
        tmp//= 2
        count+=1
    index = N - (2**(count-1)-1)
    print(2*index - 1)

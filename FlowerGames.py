import math
T = int(input())
for i in range(T):
    N = int(input())
    if N == 1:
        print(N)
    else:
        x = math.pow(2, math.floor(math.log(N)/math.log(2)))
        result = (N - (x//1)) * 2 + 1
        print(int(result//1))


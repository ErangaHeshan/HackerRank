T = int(input())

for test_case in range(T):
    N, K = [int(x) for x in input().split()]
    size_array = []
    for i in range(N):
        size_array.append(int(input()))
    size_array.sort()
    dif_size = []
    for i in range(N-1):
        dif_size.append(size_array[i+1] - size_array[i])
    dif_size.sort()
    min_sum = 0
    for i in range(len(dif_size) - K + 1):
        min_sum += dif_size[i]
    print(min_sum)

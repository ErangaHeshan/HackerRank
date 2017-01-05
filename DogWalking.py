N, K = [0, 0]
dif_NK = 0
size_array = []
matrix = []


def cal_min(left_dogs, left_walkers):
    global N
    global K
    global dif_NK
    global size_array
    global matrix

    index_begin = N - left_dogs

    if matrix[left_dogs-1][left_walkers-1] == -1:
        if left_walkers == 1:
            matrix[left_dogs-1][left_walkers-1] = size_array[N-1] - size_array[index_begin]
            result = matrix[left_dogs - 1][left_walkers - 1]
        else:
            for i in range(left_dogs-left_walkers+1, 0, -1):
                result = size_array[index_begin + i - 1] - size_array[index_begin]
                if left_walkers > 1:
                    result += cal_min(left_dogs - i, left_walkers -1)
                if matrix[left_dogs-1][left_walkers-1] == -1:
                    matrix[left_dogs - 1][left_walkers - 1] = result
                    if result == 0:
                        return 0
                else:
                    matrix[left_dogs - 1][left_walkers - 1] = min(result, matrix[left_dogs - 1][left_walkers - 1])
            result = matrix[left_dogs - 1][left_walkers - 1]

        return result
    else:
        return matrix[left_dogs-1][left_walkers-1]

T = int(input())
for test_cases in range(T):
    N, K = [int(x) for x in input().split()]
    dif_NK = N - K
    min_sum = 0
    size_array = []
    matrix = [[-1] * K for _ in range(N)]
    for size_input in range(N):
        size_array.append(int(input()))
    size_array.sort()
    print(cal_min(N, K))





T = int(input())

for i in range(T):
    input()
    array = [int(x) for x in input().split()]
    if max(array) <= 0:
        print(max(array), max(array))
    else:
        dup_array = []
        tmp = None
        
        for j in range(len(array)):
            if j == 0:
                tmp = array[j]
            elif tmp >= 0 and array[j] >= 0:
                tmp += array[j]
            elif tmp >= 0 and array[j] < 0:
                dup_array.append(tmp)
                tmp = array[j]
            elif tmp < 0 and array[j] < 0:
                tmp += array[j]
            elif tmp < 0 and array[j] > 0:
                dup_array.append(tmp)
                tmp = array[j]
            if j == len(array) - 1:
                dup_array.append(tmp)

        max_subsequent1 = 0
        max_subsequent2 = 0
        positive_sum = 0
        
        for j in range(len(dup_array)):
            max_subsequent1 = 0
            for k in range(j, len(dup_array)):
                tmp = max_subsequent1 + dup_array[k]
                if max_subsequent2 < tmp:
                    max_subsequent2 = tmp
                if tmp > 0:
                    max_subsequent1 += dup_array[k]
                else:
                    max_subsequent1 = 0
                    break

        print(max(max_subsequent1, max_subsequent2), positive_sum)



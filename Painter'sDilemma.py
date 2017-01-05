T = int(input())
for i in range(T):
    b1, b2 = -1, -1
    count = 0
    N = int(input())
    c_list = [int(x) for x in input().split()]
    for j in range(N):
        if b1 == c_list[j] or b2 == c_list[j]:
            continue
        else:
            count += 1
            for k in range(j+1, N):
                if b1 == c_list[k]:
                    b2 = c_list[j]
                    break
                elif b2 == c_list[k]:
                    b1 = c_list[j]
                    break
                elif k == N-1:
                    b1 = c_list[j]
    print(count)
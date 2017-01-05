N = int(input())
mesh = [[-1]*N for n in range(N)]
d_mesh = [[-1]*N for n in range(N)]
count = 0
# blocked = -1
# open = 0
# traversed = 1

if N>500:
    print("-1")
    exit()
def find(xx, yy):
    global N
    global d_mesh
    if xx == N - 1:
        return True
    else:
        if xx < 0 or xx > N - 1 or yy < 0 or yy > N - 1:
            return False
        else:
            if d_mesh[xx][yy] == 1 or d_mesh[xx][yy] == -1:
                return False
            else:
                d_mesh[xx][yy] = 1
                result = find(xx-1, yy) or find(xx, yy-1) or find(xx+1, yy) or find(xx, yy+1)
                return result

input_list = []
while(True):
    input_string = input()
    if input_string == "-1":
        input_list.append(int(input_string))
        # print("-1")
        break
    else:
        x, y = [int(i) for i in input_string.split()]
        input_list.append([x, y])
        # count += 1
        # mesh[x-1][y-1] = 0
        # if count >= N and (0 in mesh[0]) and (0 in mesh[N-1]):
        #     for i in range(N):
        #         if mesh[0][i] == 0:
        #             d_mesh = [i[:] for i in mesh]
        #             if find(0, i):
        #                 print(count)
                        # exit()
# print(input_list)
for i in range(len(input_list)-1, N-1, -1):
    mesh = [[-1] * N for n in range(N)]
    for j in range(i):
        mesh[input_list[j][0]-1][input_list[j][1]-1] = 0
    d_mesh = [i[:] for i in mesh]
    for k in range(N):
        if mesh[0][k] == 0:
            d_mesh = [l[:] for l in mesh]
            if find(0, k):
                count = i
                break
if count == 0:
    print("-1")
else:
    print(count)
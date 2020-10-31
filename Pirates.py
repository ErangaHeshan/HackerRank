N, M, Q = [int(x) for x in input().split()]
x1, y1, x2, y2 = [0, 0, 0, 0]
pirate_map = [[0 for x in range(M)] for y in range(N)]

for i in range(N):
    pirate_map[i] = list(input())
for i in range(Q):
    matrix = [[1001 for x in range(M)] for y in range(N)]
    x1, y1, x2, y2 = [(int(x)-1) for x in input().split()]

def process_pile(x, y):
    // TODO

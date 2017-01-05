def gcd_two(a, b):
    if matrixGCD[a][b] == -1:
        if b == 0:
            matrixGCD[a][b] = a
            return a
        else:
            matrixGCD[a][b] = gcd_two(b, a % b)
            return matrixGCD[a][b]
    else:
        return matrixGCD[a][b]


def check(c):
    if c == 1:
        return 1
    else:
        return 0

totals = []
_list = []
maxN = 0
students = int(input())
for index in range(students):
    _list.append([int(x) for x in input().split()])
    maxN = max(maxN, _list[index][0])

matrixGCD = [[-1 for x in range(maxN+1)] for y in range(maxN+1)]

for index in range(students):
    N, A, B = _list[index]
    total = 0
    for number in range(A, B+1):
        if check(gcd_two(N, number) == 1):
            if total > 1000000007:
                total = (total + number) % 1000000007
            else:
                total = total + number
    totals.append(total % 1000000007)

for index in range(students):
        print(totals[index])

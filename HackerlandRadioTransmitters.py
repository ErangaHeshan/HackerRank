#!/bin/python3

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
x = [int(x_temp) for x_temp in input().strip().split(' ')]
x.sort()
t_count = 0
prev_t = 0
distance = 0
for i in range(n - 1):
    if prev_t != 0:
        if x[i] > prev_t + k:
            distance += x[i + 1] - x[i]
            if distance > k:
                t_count += 1
                prev_t = x[i]
                distance = 0
        if i == n - 2 and x[i + 1] > prev_t + k:
            t_count += 1
    else:
        distance += x[i + 1] - x[i]
        if distance > k:
            t_count += 1
            prev_t = x[i]
            distance = 0
if n == 1:
    t_count += 1
print(t_count)

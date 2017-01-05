def fact(num):
    for i in range(1, num + 1):
        factorial = factorial * i
    return factorial

T = int(input())
for i in range(T):
    text = input().split()
    n = int(text[0])
    word = text[1]
    count = 0
    for j in range(len(word)//2):
        if word[len(word)-j-1] != word[j]:
            count += 1
    print(count)
    if n < count:
        print(0)
    elif n == count:
        print(count * 2 % 1000000007)
    else:
        result = count * 2 % 1000000007 + (26-count) ** (n-count)% 1000000007
        if len(word) % 2 == 1:
            result = result * 25 % 1000000007
        print(result)



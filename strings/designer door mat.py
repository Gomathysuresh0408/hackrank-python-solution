N, M = map(int, input().split())

# Top half
for i in range(N // 2):
    pattern = ('.|.' * (2 * i + 1)).center(M, '-')
    print(pattern)

# Middle line
print('WELCOME'.center(M, '-'))

# Bottom half
for i in range(N // 2 - 1, -1, -1):
    pattern = ('.|.' * (2 * i + 1)).center(M, '-')
    print(pattern)
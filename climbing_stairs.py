# 4-1
# 3-2
# 2-3
# 1-5
# 0-8

def climbing_stairs(n):
    a, b = 1, 1

    for _ in range(n-1, 0, -1):
        c = a + b
        a = b
        b = c
    
    return b

print(climbing_stairs(6))
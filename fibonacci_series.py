def fibonacci(n):
    if n==1:
        return 1
    
    if n==0:
        return 0
    
    a, b = 0, 1
    for _ in range(n-1):
        c = a+b
        a = b
        b = c
    return b


def fibonacci_rec(n):
    if n==1:
        return 1
    
    if n==0:
        return 0
    
    return fibonacci_rec(n-1) + fibonacci_rec(n-2)


def fibonacci_hash_map(n, dp = {1: 1, 0: 0}):
    if n in dp:
        return dp[n]
   
    dp[n] = fibonacci_hash_map(n-1, dp) + fibonacci_hash_map(n-2, dp)
    return dp[n]


n = 5
print(fibonacci(n))
print(fibonacci_rec(n))
print(fibonacci_hash_map(n))
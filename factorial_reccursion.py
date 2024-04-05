# To find the factorial of a given Number
# here I am using a Reccursive function
# So just assume find factorial of n
# just return n * call same functon with argument as n-1


def findFactorial(n):
    if n == 1:
        return n
    return n * findFactorial(n - 1)

print(findFactorial(5))
#   *
#  ***
# *****

# outer loop with number of rorw

def pyramid(n):
    for i in range(n):
        # Print spaces before the stars
        for _ in range(n - i - 1):
            print(" ", end="")
        # Print stars
        for _ in range(2 * i + 1):
            print("*l", end="")
        print()

pyramid(10)


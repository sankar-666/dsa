# we need to reverse a sting usng reccursion
# time complxity will be O(n^2)
# create a fn with 1 arg string
# slice last letter a store it in a variable
# call the same fn and pass the remaning string
# return the output sting after the normal sting length is 0

# Normal Approch
reversedString = ""
def recursiveStringReverse(text):
    global reversedString
    if len(text) == 0:
        return reversedString

    # Use text[-1] to get the last character
    reversedString += text[-1]

    # Correct the slicing, use text[:-1] to exclude the last character
    return recursiveStringReverse(text[:-1])

# Better Approch
def recursive_reverse_string(text):
    if not text:
        return text
    else:
        return text[-1] + recursive_reverse_string(text[:-1])



result = recursive_reverse_string('sankar')
print(result)
result = recursiveStringReverse('this is london')
print(result)


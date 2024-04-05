# we need to calculate count of letters in a sorted string 
# and return out string as letter, count , letter, count ...
# we can simple loop through sting and get the count using a hashMap
# and loop through the  hashMap to get final result
# O(n) ts
from collections import Counter
def convertToCountString(str_input) -> str:
    char_count_map= {}

    # get the count from input string
    for i in  range(len(str_input)):
        char_count_map[str_input[i]] = char_count_map.get(str_input[i], 0) + 1
        
    result = []
    # loop the entire map to get each letters and their count
    for key in char_count_map.keys():
        result.append(key + str(char_count_map.get(key)))

    # better Approch
    # char_count_map = Counter(str_input)
    # result = [char + str(count) for char, count in char_count_map.items()]

    # convert the list to string and return
    return "".join(result)

print(convertToCountString("aaabbbbbbcccd"))
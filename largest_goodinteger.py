def largestGoodInteger(num):
    # solve this using hashmap
    map = {}
    map2 = {}
    for i in num:
        map[i] = (map.get(i, 0)) + 1
    
    for j in map:
        if map[j] >= 3:
            map2[j] = map[j]

    print(map)
    print(map2)
    if not map2:
        return ""  # Return an empty string if no good integer is found
    
    max_key = 0
    for key in map2.keys():
        key = int(key)
        print(key)
        # Check if key, key+1, and key-1 are present in the string
        if str(key) in num and str(key + 1) in num and str(key - 1) in num:
            # Check if they appear consecutively
            if num.index(str(key)) == num.index(str(key + 1)) == num.index(str(key - 1)):
                max_key = max(max_key, key)
    if max_key == 0:
        return ""
            
    return str(max_key) * map[str(max_key)]

result = largestGoodInteger('677771333399999999')
print(result)

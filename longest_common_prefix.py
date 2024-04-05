def longest_common_prefix(strs):
    if not strs:
        return ""
    
    # Assume the first string as the prefix to start with
    prefix = strs[0]
    
    # Iterate through the strings starting from the second one
    for string in strs[1:]:
        # Update the prefix by comparing characters with each string
        while string[:len(prefix)] != prefix:
            prefix = prefix[:len(prefix) - 1]
            if not prefix:  # If the prefix becomes empty, no common prefix exists
                return ""
    
    return prefix

# Example usage:
strs = ["flower", "flow", "flight"]
print(longest_common_prefix(strs))  # Output: "fl"

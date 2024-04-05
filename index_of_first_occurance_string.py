class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)

sol = Solution()
print(sol.strStr("sadbutsad", "sad")) 
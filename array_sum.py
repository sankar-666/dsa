# given a array and target, we need to find the target from the array sum
# we can solve using hashmap
# assume first element as x and y = target-x
# if (y in map) return [x, y]
# else add y to map
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, x in enumerate(nums):
            y = target - x
            if y in map:
                return [map[y], i]
            map[x] = i

sol = Solution()

print(sol.twoSum([2,7,11,15], 9))
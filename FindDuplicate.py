
from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myMap = {}

        for i, n in enumerate(nums):
            if n in myMap:
                return True  # 'true' should be 'True'
            myMap[n] = i
        
        return False  # 'false' should be 'False'


if __name__ == "__main__":
    solution = Solution()

    nums = [2,7,11,15]
    

    result = solution.hasDuplicate(nums)
    print (result)
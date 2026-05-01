class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        for x in nums:
            repeat = 0
            for y in nums:
                if x == y: repeat = repeat + 1
            if repeat > 1: return True

        
        return False



        
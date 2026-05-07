class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashNum = {}
        
        for i, n in enumerate(nums):
            x = target - n
            if x in hashNum:
                return [hashNum[x], i]
            hashNum[n] = i
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_num = list(set(nums))
        count = 0
        if len(new_num) == len(nums):
            return False
        for i in range(len(nums)):
            for j in range(len(new_num)):
                if new_num[j] == nums[i]:
                    count+=1
        if count>=2:
            return True
        return False 
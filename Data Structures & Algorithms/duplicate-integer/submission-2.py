class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[j] == nums[i]:
        #             return True
        # return False

        # ---------------------------------

        # if len(set(nums)) == len(nums):
        #     return False
        # else:
        #     return True
        # ----------------------------

        seen = set()
        for num in nums :
            if num in seen :
                return True
            else:
                seen.add(num)

        return False
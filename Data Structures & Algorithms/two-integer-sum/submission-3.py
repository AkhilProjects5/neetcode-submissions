class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(0,len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if  nums[i] + nums[j] == target:
        #             return ([i,j])
        
        # ----------------------------------------
        dict_num = {}
        for num in range(0,len(nums)):
            dict_num[nums[num]] = num
        
        for num in range(len(nums)):
            if (target - nums[num]) in dict_num.keys():
                if num != dict_num[target - nums[num]]:
                    return([num , dict_num[target - nums[num]]])

                
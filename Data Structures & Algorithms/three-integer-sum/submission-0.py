class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result_list = []
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i]+nums[j]+nums[k] == 0 and sorted([nums[i],nums[j],nums[k]]) not in result_list:
                        result_list.append(sorted([nums[i],nums[j],nums[k]]))

        return result_list
        
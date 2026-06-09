class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # result_list = []
        # for i in range(0,len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1,len(nums)):
        #             if nums[i]+nums[j]+nums[k] == 0 and sorted([nums[i],nums[j],nums[k]]) not in result_list:
        #                 result_list.append(sorted([nums[i],nums[j],nums[k]]))

        # return result_list

        # --------------------------------------------
        
        result_list = []
        nums = sorted(nums)
        for k in range(len(nums)):
            i,j= k+1,len(nums)-1
            while i<j:
                if nums[k] + nums[i] + nums[j] == 0 :
                    if [nums[k],nums[i],nums[j]] in result_list :
                        pass
                    else:
                        result_list.append([nums[k],nums[i],nums[j]])
                    i +=1
                elif nums[k] + nums[i] + nums[j] > 0 :
                    j -=1
                else:
                    i +=1
        return result_list
            



        
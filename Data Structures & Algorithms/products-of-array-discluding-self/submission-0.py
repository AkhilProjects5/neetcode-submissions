class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        multiple_list = []
        

        for i in range(len(nums)):
            multiplication = 1
            for j in range(len(nums)):
                if i!=j:
                    multiplication = multiplication * nums[j]
            multiple_list.append(multiplication)
        return multiple_list
        
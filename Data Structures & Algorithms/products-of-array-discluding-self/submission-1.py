class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # multiple_list = []
        left_product = 1
        right_product = 1
        # for i in range(len(nums)):
            # multiplication = 1
            # for j in range(len(nums)):
            #     if i!=j:
            #         multiplication = multiplication * nums[j]
            # multiple_list.append(multiplication)
        multiple_list = [1]*len(nums)
        for i in range(len(nums)):
            multiple_list[i] = left_product
            left_product = left_product*nums[i]

        for i in range(len(nums)-1,-1,-1):
            multiple_list[i] = multiple_list[i]*right_product
            right_product = right_product*nums[i]

        return multiple_list
        
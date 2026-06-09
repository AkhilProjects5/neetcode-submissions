class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = [0]*len(nums)
        counter_i = 0
        for i in range(len(nums)) :
            if nums[i] == 1:
                counter_i = counter_i + 1
            else:
                counter.append(counter_i)
                counter_i = 0
        counter.append(counter_i)
        return max(counter)

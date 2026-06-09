class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        sum_set = sum(nums)

        if sum_set%2 != 0:
            return False
        
        total = sum_set//2

        t = [[False for _ in range(total+1)] for _ in range(n+1)]

        for i in range(n+1):
            for j in range(total+1):
                if i == 0 :
                    t[i][j] = False
                elif j == 0:
                    t[i][j] = True
                else:
                    if nums[i-1] <= j :
                        t[i][j] = t[i-1][j-nums[i-1]] or t[i-1][j]
                        

                    else:
                        t[i][j] = t[i-1][j]


        return t[n][total]

        
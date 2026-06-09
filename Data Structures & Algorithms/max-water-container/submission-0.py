class Solution:
    def maxArea(self, heights: List[int]) -> int:
        greatest_area = 0
        i,j = 0,len(heights)-1
        while i<j:
            current_area = min(heights[i],heights[j])*(j-i)
            if  current_area > greatest_area:
                greatest_area = current_area
            
            if heights[i]>heights[j]:
                j -=1
            elif heights[i] < heights[j]:
                i +=1
            else:
                j -=1
                i +=1
        
        return greatest_area
        
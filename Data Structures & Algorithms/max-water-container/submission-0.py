class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        max_area = 0
        while i<j :
            tmp_area = (j-i)*min(heights[i],heights[j])
            max_area = max(max_area, tmp_area)
            if heights[i] < heights[j]:
                i+=1
            elif  heights[j] < heights[i]: 
                j-=1
            else:
                if heights[i+1] < heights[j-1]:
                    j-=1
                elif heights[i+1] > heights[j-1]:
                    i+=1
                else:
                    i+=1
                    j-=1
        return max_area


        
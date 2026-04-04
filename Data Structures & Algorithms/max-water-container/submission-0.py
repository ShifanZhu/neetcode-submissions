class Solution:
    def maxArea(self, heights: List[int]) -> int:
        heights_len = len(heights)
        print("len: ", heights_len)

        max_area = 0
        for i in range(heights_len):
            for j in range(i+1, heights_len):
                area = min(heights[i], heights[j]) * (j - i)
                if area > max_area:
                    max_area = area
        
        return max_area

        
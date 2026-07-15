class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left_boudaries = [0 for i in range(n)]
        right_boudaries = [0 for i in range(n)]
        
        max_area = -float("inf")


        left_boudaries[0] = -1
        for i in range(1, n):
            boundary = i - 1

            while (boundary > -1 and heights[boundary] >= heights[i]):
                boundary = left_boudaries[boundary]

            left_boudaries[i] = boundary



        right_boudaries[n - 1] = n 

        for i in range(n - 2, -1, -1):
            boundary = i + 1

            while (boundary < n and heights[boundary] >= heights[i]):
                boundary = right_boudaries[boundary]

            right_boudaries[i] = boundary


        for i in range(len(heights)):
            area = heights[i] * (right_boudaries[i] - left_boudaries[i] - 1)
             
            if area > max_area:
                max_area = area


        return max_area







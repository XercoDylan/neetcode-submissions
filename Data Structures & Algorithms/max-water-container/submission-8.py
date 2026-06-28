class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = -float("inf")
        lower = 0
        upper = len(heights) - 1

        while (lower < upper):
            area = min(heights[lower], heights[upper]) * (upper - lower)

            if area > maximum:
                maximum = area

            if heights[lower] < heights[upper]:
                lower += 1
            else:
                upper -= 1

        
        return maximum


        
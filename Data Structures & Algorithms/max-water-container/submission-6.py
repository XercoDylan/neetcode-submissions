class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        highest = -float('inf')


        while (left < right):

            area = (right - left) * min(heights[left], heights[right])

            if area > highest:
                highest = area

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1


        return highest
        
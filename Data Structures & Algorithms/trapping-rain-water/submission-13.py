class Solution:
    def trap(self, height: List[int]) -> int:
        highest_left = []
        highest_right = []
        total = 0

        for i in range(len(height)):
            if len(highest_left) == 0:
                highest_left.append(height[i])
            else:
                if height[i] > highest_left[-1]:
                    highest_left.append(height[i])
                else:
                    highest_left.append(highest_left[-1])

        for i in range(len(height) - 1, -1, -1):
            if len(highest_right) == 0:
                highest_right.append(height[i])
            else:
                if height[i] > highest_right[-1]:
                    highest_right.append(height[i])
                else:
                    highest_right.append(highest_right[-1])

        for i in range(len(height)):
            total += min(highest_left[i], highest_right[len(height) - 1 - i]) - height[i]


        return total
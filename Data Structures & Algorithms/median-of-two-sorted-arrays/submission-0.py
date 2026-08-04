class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arrayA = nums1 if len(nums1) > len(nums2) else nums2
        arrayB = nums2 if arrayA == nums1 else nums1
        total = len(arrayA) + len(arrayB)
        half = (total)//2


        low = 0
        high = len(arrayB)

        while (low <= high):
            choosen_B = low + (high - low)//2
            choosen_A = half - choosen_B

            max_left_B = -float("inf") if choosen_B == 0 else arrayB[choosen_B - 1]

            next_B = float("inf") if choosen_B == len(arrayB) else arrayB[choosen_B]


            max_left_A = -float("inf") if choosen_A == 0 else arrayA[choosen_A - 1]

            next_A = float("inf") if choosen_A == len(arrayA) else arrayA[choosen_A]

            if (max_left_B <= next_A and max_left_A <= next_B):
                if total%2 == 1:
                    return min(next_A, next_B) 
                else:
                    return (min(next_A, next_B) + max(max_left_A,max_left_B) )/2
            elif (max_left_B > next_A):
                high = choosen_B - 1
            else:
                low = choosen_B + 1

            
            



        
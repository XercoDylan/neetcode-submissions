class Solution:
    def calculate_required_hours(self, k: int, piles: List[int]):
        total_time = 0

        for bannanas in piles:
            total_time += -(-bannanas//k)

        return  total_time

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high = -float("inf")
        for k in piles:
            if k > high:
                high = k

        low = 1
        minimum_k = 0

        while (low <= high):
            mid = low + (high - low)//2


            required_h = self.calculate_required_hours(mid, piles)
            print(f"{mid} {required_h}")

            if required_h <= h:
                minimum_k = mid
                high = mid - 1
            else:
                low = mid + 1

        return minimum_k
                
            

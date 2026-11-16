
import math

class Solution:
    def minEatingSpeed(self, piles, h):
        low = 1
        high = max(piles)

        while low < high:
            mid = (low + high) // 2

            hours = 0
            for p in piles:
                hours += math.ceil(p / mid)

            if hours <= h:
                high = mid
            else:
                low = mid + 1

        return low

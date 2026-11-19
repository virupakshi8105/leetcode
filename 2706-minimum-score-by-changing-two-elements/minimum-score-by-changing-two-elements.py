
class Solution:
    def minimizeSum(self, nums):
        nums.sort()
        n = len(nums)

        if n <= 3:
            return 0

        ans = float('inf')

        for i in range(3):
            ans = min(ans, nums[n - 3 + i] - nums[i])

        return ans

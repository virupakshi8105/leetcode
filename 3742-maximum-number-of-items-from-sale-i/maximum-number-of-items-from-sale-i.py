from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        bonus = []

        for i in range(n):
            count = 0
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    count += 1
            bonus.append(count)

        dp = [0] * (budget + 1)

        for i in range(n):
            price = items[i][1]
            gain = 1 + bonus[i]

            for b in range(budget, price - 1, -1):
                dp[b] = max(dp[b], dp[b - price] + gain)

            for b in range(price, budget + 1):
                dp[b] = max(dp[b], dp[b - price] + 1)

        return max(dp)
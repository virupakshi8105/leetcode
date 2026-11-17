class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')

        # cost[i][j]: minimum changes to make s[i..j] a semi-palindrome
        cost = [[INF] * n for _ in range(n)]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                best = INF

                # d is the chosen divisor; d < length
                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0

                    # For each residue class modulo d,
                    # make the characters form a palindrome.
                    for r in range(d):
                        left = i + r
                        right = i + r + ((length - 1 - r) // d) * d

                        while left < right:
                            if s[left] != s[right]:
                                changes += 1
                            left += d
                            right -= d

                    best = min(best, changes)

                cost[i][j] = best

        # dp[p][i]: minimum changes to split first i characters into p parts
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for p in range(1, k + 1):
            for i in range(2 * p, n + 1):
                # Previous cut must leave at least 2 characters
                # for the current substring.
                for j in range(2 * (p - 1), i - 1):
                    if dp[p - 1][j] == INF:
                        continue

                    dp[p][i] = min(
                        dp[p][i],
                        dp[p - 1][j] + cost[j][i - 1]
                    )

        return dp[k][n]
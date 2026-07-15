class Solution:
    def coinChange(self, coins, amount):

        dp = {}

        def solve(rem):

            if rem == 0:
                return 0

            if rem < 0:
                return float('inf')

            if rem in dp:
                return dp[rem]

            ans = float('inf')

            for coin in coins:
                ans = min(ans, 1 + solve(rem - coin))

            dp[rem] = ans
            return ans

        ans = solve(amount)
        return -1 if ans == float('inf') else ans
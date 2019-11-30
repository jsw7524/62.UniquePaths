class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (m+1) for i in range(n+1)]
        for i in range(m + 1):
            dp[1][i]=1
        for j in range(2,n+1):
            for i in range(1,m+1):
                dp[j][i] = dp[j-1][i]+dp[j][i-1]
        return dp[n][m]

sln=Solution()
assert 3==sln.uniquePaths(3,2)

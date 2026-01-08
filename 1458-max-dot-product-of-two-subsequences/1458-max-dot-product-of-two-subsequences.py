class Solution:
    def maxDotProduct(self, nums1: list[int], nums2: list[int]) -> int:
        m, n = len(nums1), len(nums2)
        # Initialize DP table with a very small value
        dp = [[-float('inf')] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                curr_prod = nums1[i-1] * nums2[j-1]
                
                # Option 1: Current product + best previous dot product (or just current product)
                # Option 2: Best without current nums1 element
                # Option 3: Best without current nums2 element
                dp[i][j] = max(
                    curr_prod,
                    curr_prod + dp[i-1][j-1],
                    dp[i-1][j],
                    dp[i][j-1]
                )
                
        return dp[m][n]
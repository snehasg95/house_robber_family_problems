# Optimised solution, similar to house robber 1 - O(N) Time and Space O(N) as we use a dp array
class Solution:
    def rob(self, houses: List[int]) -> int:
        
        if not houses:
            return 0
        
        if len(houses) == 1:
            return houses[0]
        
        if len(houses) == 2:
            return max(houses)
        
        
        return max(self.helper(houses[1:]), self.helper(houses[:-1]))
    
    
    def helper(self, houses):
        
        rows = len(houses)
        cols = 2
        
        dp = [[0] * cols for i in range(rows)]
        dp[0][1] = houses[0]
        
        for i in range(1, rows):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            
            dp[i][1] = dp[i-1][0] + houses[i]
            
        return max(dp[rows-1][0], dp[rows-1][1])
        
        
        
 
# O(N) Time and O(1) space solution
class Solution:
    def rob(self, houses: List[int]) -> int:
        
        
        if not houses:
            return 0
        
        if len(houses) == 1:
            return houses[0]
        
        
        return max(self.helper(houses[1:]), self.helper(houses[:-1]))
    
    
    
    def helper(self, nums):
        
        prev = 0
        current = 0
        
        for num in nums:
            temp = prev
            prev = current
            current = max(current, num + prev)
            
        return current
        
        
        
        
  
            

# Brute Force - recursive choose no choose solution - O(T) is 2^N 2 choices at each node
# [1,2,3,1] - max profit 4

class Solution:
    def rob(self, houses: List[int]) -> int:
      
      # base case
      
      if not houses:
        return 0

        
      return self.helper(houses, 0, 0)
    
    def helper(self, nums, index, profit): 
        #int function not void
        
        #base case
        if index >= len(nums):
            # >= as at choose we skip 2 indices leading to possible out of bounds
            return profit
        
        #logic 
        
        #dont choose
        no_rob = self.helper(nums, index + 1, profit)
        
        # choose
        # skip 2 indices and add to profit what you robbed
        rob = self.helper(nums, index + 2, profit + nums[index])
        
        return max(no_rob, rob)
    
      
     
# Optimised - Same as above in a tabular form so we also memoize and save on recursive call stack
class Solution:
    def rob(self, houses: List[int]) -> int:
      
        if not houses:
            return 0
        
        rows = len(houses)
        cols = 2 # no choose & choose
        
        dp = [[0] * cols for i in range(rows)]
        
        dp[0][1] = houses[0] # base case for robbing at first time
        
        for i in range(1, len(houses)):
            
            # dont choose (max between previous dont rob and rob previous amount - if the dont choose takes precedence than choosing this is better, if 
            # choose prev contrinutes to max, not choosing this val is better
            
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            
            # choose 
            # add this current value to previous dont robb choice, ie we skipped previous to add this current one
            dp[i][1] = dp[i-1][0] + houses[i]
            
            
            
 class Solution:
    def rob(self, houses: List[int]) -> int:
      
      if not houses:
            return 0
        
        if len(houses) == 1:
            return houses[0]
        
        profits = houses[:]
        profits[1] = max(profits[0], profits[1])
        
        for i in range(2, len(houses)):
            profits[i] = max(profits[i-1], profits[i] + profits[i-2])
            
            
        return profits[-1]
  


## More optimised

# O(N) time and O(1) space
class Solution:
    def rob(self, houses: List[int]) -> int:
        
        if not houses:
            return 0
        
        if len(houses) == 1:
            return houses[0]
        
        prevMax = 0
        currentMax = 0
        
        for i in range(len(houses)):
            
            temp = currentMax
            currentMax = max(currentMax, prevMax + houses[i])
            
            prevMax = temp
            
            
        return currentMax

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
        
        
        
        
        
        
        
        
# Attempt 1 d solution        
#         if not houses:
#             return 0
        
#         self.profits = []
        
        
#         for i in range(0, len(houses) - 1):
#             if len(houses) == 1:
#                 return houses[0]



#             profits = houses[0:len(houses) - 1]
#             print(profits)
#             profits[1] = max(profits[0], profits[1])

#             for i in range(1, len(houses)):
#                 profits[i] = max(profits[i-1], profits[i] + profits[i-2])


#             self.profits.append(profits[-1])
            
            
            
#         for i in range(2, len(houses)):
            
#             if len(houses) == 1:
#                 return houses[0]



#             profits = houses[2]
#             profits[1] = max(profits[0], profits[1])

#             for i in range(2, len(houses)):
#                 profits[i] = max(profits[i-1], profits[i] + profits[i-2])


#             self.profits.append(profits[-1])
            
            
#         print(self.profits)   
#         return max(self.profits)
            
            

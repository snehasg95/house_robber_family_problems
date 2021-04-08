class Solution:
    def deleteAndEarn(self, values: List[int]) -> int:
        
        if not values:
            return 0
        
        max_val = 0
        
        # preprocessing data to group all occurrences of a number cumulative
        aux_arr = [0] * (max(values) + 1)
      

        for num in values:
            aux_arr[num] += num
        
        print(aux_arr)
        
        
        # now reduced to house problem, where if we rob one the adjacent ones(that is here the ones greater than or - should be deleted, as in skip those values)
        
        prev = 0
        current = 0
        
        for num in aux_arr:
            temp = prev
            prev = current
            current = max(current, temp + num)
            
        return current

      
      
      ######## Another solution
        # this solution is based off the dp array solution we solved exactly
        skip = 0
        take = aux_arr[0]

        for i in range(len(aux_arr)):
            temp = skip

            skip = max(skip, take)
            take = temp + aux_arr[i]

        return max(skip, take)
        

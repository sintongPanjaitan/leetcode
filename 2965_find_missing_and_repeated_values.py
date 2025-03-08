class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        num_count = {}
        repeat = None
        missing = None
        n = len(grid) * len(grid[0])
        num_count = [0] * (n + 1)
        
        for row in grid:
            for num in row:
                num_count[num] += 1
        
        for i in range(1, n + 1):
            if num_count[i] == 0:
                missing = i
            elif num_count[i] == 2:
                repeat = i
        
        return [repeat, missing]
# Time: O(n^2)
# Space: O(n)

print(Solution().findMissingAndRepeatedValues([[1,3],[2,2]])) # [2, 4]
print(Solution().findMissingAndRepeatedValues([[9,1,7],[8,9,2],[3,4,6]])) # [9,5]
# Time: O(n)    


                
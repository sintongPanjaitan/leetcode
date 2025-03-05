class Solution(object):
    def coloredCells(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 2 * n * (n - 1) + 1
        
# Time: O(1)
# Space: O(1)

print(Solution().coloredCells(1)) # 1
print(Solution().coloredCells(2)) # 5
print(Solution().coloredCells(3)) # 13
class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        temp= []
        n=0
        while n <= len(blocks) - k: 
            j = 0
            temp_w = []
            for i in range(n, len(blocks)):
                if j == k:
                    break
                if blocks[i] == "W":
                    temp_w.append(i)
                j+=1
            if n>0:
                if len(temp_w) < len(temp):
                    temp = temp_w
            else:
                temp = temp_w
            n+=1
        return len(temp)
        
print(Solution().minimumRecolors("WBBWWBBWBW", 7)) # 3
print(Solution().minimumRecolors("WBWBBBW", 2)) # 0
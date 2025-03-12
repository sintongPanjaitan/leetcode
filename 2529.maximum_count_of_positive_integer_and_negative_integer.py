class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        positive = 0
        negative = 0
        for i in nums:
            if i == 0:
                continue
            if i >0 :
                positive += 1
            else:
                negative += 1
        return max(positive, negative)

print(Solution().maximumCount([-2,-1,-1,1,2,3])) # 3
print(Solution().maximumCount([1,1,0,0,0])) # 2
print(Solution().maximumCount([-1,-1,-1,-1,-1])) # 5
print(Solution().maximumCount([1,2,3,4,5])) # 5
print(Solution().maximumCount([0,0,0,0,0])) # 0
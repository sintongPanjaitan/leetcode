class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        result = []
        left_side = []
        right_side = []
        middle_side = []
        for num in nums:
            if num < pivot:
                left_side.append(num)
            elif num == pivot:
                middle_side.append(num)

            else:
                right_side.append(num)
                
           
        result = left_side + middle_side + right_side
        return result


if __name__ == '__main__':
    nums = [9,12,5,10,14,3,10]
    pivot = 10
    
    print(Solution().pivotArray(nums=nums,pivot=pivot))
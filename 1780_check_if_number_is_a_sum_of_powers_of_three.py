class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 0:
            if n % 3 == 2:
                return False
            n //= 3
        return True

if __name__ == '__main__':
    print(Solution().checkPowersOfThree(12))
    print(Solution().checkPowersOfThree(91))
    print(Solution().checkPowersOfThree(21))
    print(Solution().checkPowersOfThree(24))
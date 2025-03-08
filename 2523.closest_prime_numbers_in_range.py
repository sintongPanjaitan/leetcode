
class Solution(object):
    def closestPrimes(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        two_prime_number = []
        prime_number = []
        for i in range(left, right+1):
            if i == 1:
                continue

            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    break
            else:
                two_prime_number.append(i)
            
            if len(two_prime_number) == 2:
                if two_prime_number[1]-two_prime_number[0] <= 2:
                    return two_prime_number
                prime_number.append(two_prime_number)
                two_prime_number=[two_prime_number[1]]
        
        if len(prime_number) == 1:
            return prime_number[0]
        if len(prime_number)<2:
            return [-1, -1]
        return two_prime_number


print(Solution().closestPrimes(10, 19)) # [11, 13] 
print(Solution().closestPrimes(4, 6))   # [-1, -1]
print(Solution().closestPrimes(19,31))  # [29,31] 
print(Solution().closestPrimes(1087,4441))  # [29,31] 
print(Solution().closestPrimes(850350,851803))  # [851801, 851803]
print(Solution().closestPrimes(69346,69379))  # [69371,69379]
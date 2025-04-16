class Solution(object):
    def balancedStringSplit(self, s):
        temp_dict = {
            "R":0,
            "L":0
        }
        result = 0
        for i in range(len(s)):
            temp_dict[s[i]] = temp_dict.get(s[i]) + 1

            if temp_dict.get("R") == temp_dict.get("L"):
                temp_dict["R"] = 0
                temp_dict["L"] = 0
                result = result + 1
        return result

print(Solution().balancedStringSplit(s="RLRRLLRLRL"))#4
print(Solution().balancedStringSplit(s="RLRRRLLRLL"))#2
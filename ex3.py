# https://leetcode.com/problems/container-with-most-water/

#2 poinster solution

# Driver program to test above fnction */ 
height = [3, 5, 4, 2, 6, 3, 0, 0, 5, 4, 8, 3] 
n = len(height)
print(n)
def maxArea(height):
#     """
#     :type height: List[int]
#     :rtype: int
#     """
    L, R, width, res = 0, len(height) - 1, len(height) - 1, 0
    print(L, R, width, res)
    for w in range(width, 0, -1):
        if height[L] < height[R]:
            res, L = max(res, height[L] * w), L + 1
        else:
            res, R = max(res, height[R] * w), R - 1
        print(L, R, w, height[L] , height[R],res)
    return res
maxArea(height)    


def romanToInt(self, s):
        retInt = 0
        localMax = 0
        romanDict = {"I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000}
        
        for c in reversed(s):
            val = romanDict[c];
            if localMax <= val:
                retInt += val
                localMax = val
            else:
                retInt -= val
        return retInt

def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        
        result = 0
        prev_value = 0
        for letter in s:
            value = roman_to_int[letter]
            result += value
            if value > prev_value:
                # preceding roman nummber is smaller
                # we need to undo the previous addition
                # and substract the preceding roman char
                # from the current one, i.e. we need to
                # substract twice the previous roman char
                result -= 2 * prev_value
            prev_value = value
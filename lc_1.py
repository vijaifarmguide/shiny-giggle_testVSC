

class Solution(object):

    # def __init__(self, nums, target):
    #     self.nums = nums
    #     self.target = target

    # def twoSum(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: List[int]
    #     """
    #     print(nums)
    #     print(target)
    def twoSum(self, num, target):
        map = {}
        for i in range(len(num)):
            if num[i] not in map:
                map[target - num[i]] = i + 1
            else:
                return map[num[i]], i + 1

        return -1, -1



nums = [2, 7, 11, 15]
target = 13

sol=Solution()
abc=sol.twoSum(nums,target)
print(abc)



#other solutions
# dictionary 
# def twoSum1(self, nums, target):
#     dic = {}
#     for i, num in enumerate(nums):
#         if target-num in dic:
#             return (dic[target-num]+1, i+1)
#         dic[num] = i
 
# # two-pointer       
# def twoSum(self, nums, target):
#     nums = enumerate(nums)
#     nums = sorted(nums, key=lambda x:x[1])
#     l, r = 0, len(nums)-1
#     while l < r:
#         if nums[l][1]+nums[r][1] == target:
#             return sorted([nums[l][0]+1, nums[r][0]+1])
#         elif nums[l][1]+nums[r][1] < target:
#             l += 1
#         else:
#             r -= 1



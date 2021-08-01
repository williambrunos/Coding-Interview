'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

# The idea here is calculate the complement between a value on the array and the
# target value. If this complement is in a HashMap (search complexity O(1)), then
# we return  list of the index of this complement on the hash map and the current
# index. Althought, we store the number and its index on the hash map.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashMap.keys():
                lst = [hashMap[complement], i]
                return lst
            
            hashMap[nums[i]] = i
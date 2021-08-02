'''
LEETCODE

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_list = (nums1 + nums2)
        new_list.sort()
        
        if(len(new_list) % 2 == 0):
            mid_index_next = int(len(new_list) / 2)
            mid_index_ant = mid_index_next - 1
            value = (new_list[mid_index_next] + new_list[mid_index_ant]) / 2
            return float(value)
        else:
            mid_index = int(len(new_list) / 2)
            value = new_list[mid_index]
            return float(value)
        return 0
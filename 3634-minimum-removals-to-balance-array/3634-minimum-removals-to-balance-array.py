class Solution(object):
    def minRemoval(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        left = 0
        for right in range(len(nums)):
            if nums[left]*k < nums[right]:
                left += 1
        return left

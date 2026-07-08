"""
Problem: Check if the Array is Sorted II
Difficulty: Easy
Link: https://takeuforward.org/plus/dsa/problems/check-if-the-array-is-sorted-ii
"""

class Solution:
    def isSorted(self, nums):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.isSorted([1, 2, 3]))  # Expected: True
    print(sol.isSorted([3, 2, 1]))  # Expected: False


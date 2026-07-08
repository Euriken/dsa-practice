"""
Problem: Check if Array is Sorted and Rotated
Difficulty: Easy
Link: https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/
"""

class Solution:
    def check(self, nums):
        count = 0
        for i in range(len(nums)):
            if nums[i] > nums[(i + 1) % len(nums)]:
                count += 1
        return count <= 1


if __name__ == "__main__":
    sol = Solution()
    print(sol.check([3, 4, 5, 1, 2]))  # Expected: True
    print(sol.check([2, 1, 3, 4]))     # Expected: False


"""
Problem: Largest Element
Difficulty: Easy
Link: https://takeuforward.org/plus/dsa/problems/largest-element
"""

class Solution:
    def largestElement(self, nums):
        maxi = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > maxi:
                maxi = nums[i]
        return maxi


if __name__ == "__main__":
    sol = Solution()
    print(sol.largestElement([3, 3, 6, 1]))       # Expected: 6
    print(sol.largestElement([3, 3, 0, 99, -40]))  # Expected: 99

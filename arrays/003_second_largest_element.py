"""
Problem: Second Largest Element
Difficulty: Easy
Link: https://takeuforward.org/plus/dsa/problems/second-largest-element
"""

class Solution:
    def secondLargestElement(self, nums):
        largest = nums[0]
        secondLargestElement = -1
        for i in range(len(nums)):
            if nums[i] > largest:
                secondLargestElement = largest
                largest = nums[i]
            elif nums[i] < largest and nums[i] > secondLargestElement:
                secondLargestElement = nums[i]
        return secondLargestElement


if __name__ == "__main__":
    sol = Solution()
    print(sol.secondLargestElement([8, 8, 7, 6, 5]))  # Expected: 7
    print(sol.secondLargestElement([10, 10, 10, 10, 10]))  # Expected: -1

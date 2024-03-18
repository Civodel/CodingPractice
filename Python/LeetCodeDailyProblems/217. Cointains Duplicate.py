'''Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.'''
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        for index in range(len(nums)):
            for j_index in range(index+1,len(nums)):
                if nums[index]==nums[j_index]:
                    return True

        return False







if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(Solution().containsDuplicate(nums))

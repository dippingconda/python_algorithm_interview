"""
https://leetcode.com/problems/two-sum
"""


def two_sum(nums, target):
    nums_dict = {}
    for idx, val in enumerate(nums):
        nums_dict[val] = idx

    for idx, val in enumerate(nums):
        if target - val in nums_dict and idx != nums_dict[target - val]:
            return idx, nums_dict[target - val]


def two_sum2(nums, target):
    for val in nums:
        if target - val in nums:
            return nums.index(val), nums.index(target - val)


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(f'{two_sum2(nums, target)}')
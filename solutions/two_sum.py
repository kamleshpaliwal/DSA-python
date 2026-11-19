class Solution:
    @classmethod
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, item in enumerate(nums):
            complement = target - item
            if complement in seen:
                return [seen[complement], i]
            seen[nums[i]] = i


if __name__ == "__main__":
    nums = [2, 11, 15, 7]
    target = 9
    result = Solution.twoSum(nums, target)
    print(result)

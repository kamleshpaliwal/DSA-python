class Solution:
    def isPair(self, nums: list[int], target: int) -> bool:
        low = 0
        high = len(nums) - 1
        while low < high:
            if (nums[low] + nums[high]) == target:
                return True
            elif (nums[low] + nums[high]) > target:
                high = high - 1
            else:
                low = low + 1

        return False


if __name__ == "__main__":
    solution = Solution()
    nums = [2, 5, 8, 12, 30]
    target = 1
    result = solution.isPair(nums, target)
    print("pair found", result)

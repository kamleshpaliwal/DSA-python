class Solution:
    def binary_search(self, low: int, high: int, target: int, nums: list[int]) -> bool:

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return False


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4, 5]
    low = 0
    high = len(nums) - 1
    target = 5
    result = solution.binary_search(low, high, target, nums)
    print(result)

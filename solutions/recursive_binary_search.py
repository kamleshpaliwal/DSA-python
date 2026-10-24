class Solution:
    @staticmethod
    def binary_search(nums: list[int], target: int, low: int, high: int) -> int:
        if low > high:
            return -1
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return Solution.binary_search(nums, target, low, mid - 1)
        else:
            return Solution.binary_search(nums, target, mid + 1, high)


if __name__ == "__main__":
    print(Solution.binary_search([1, 3, 5, 7, 9], 3, 0, len([1, 3, 5, 7, 9]) - 1))

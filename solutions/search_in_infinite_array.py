class Solution:
    def binary_search(self, low: int, high: int, target: int, nums: list[int]) -> int:
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1

    def find_pos(self, nums: list[int], target: int) -> int:

        if nums[0] == target:
            return 0
        i = 1
        while nums[i] <= target:
            i *= 2

        low = i // 2
        high = i
        return self.binary_search(low, high, target, nums)


if __name__ == "__main__":
    solution = Solution()
    nums = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170]
    result = solution.find_pos(nums, 5)
    if result == -1:
        print("target not found")
    else:
        print("target  found at index ", result)

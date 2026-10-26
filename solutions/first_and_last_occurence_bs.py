class Solution:
    def binary_search_first(
        self, low: int, high: int, nums: list[int], target: int
    ) -> int:
        if low > high:
            return -1
        mid = (low + high) // 2
        if nums[mid] > target:
            return self.binary_search_first(low, mid - 1, nums, target)
        elif nums[mid] < target:
            return self.binary_search_first(mid + 1, high, nums, target)
        else:
            mid1 = self.binary_search_first(low, mid - 1, nums, target)

            if mid1 == -1:
                return mid
            else:
                return mid1

    def binary_search_last(
        self, low: int, high: int, nums: list[int], target: int
    ) -> int:
        if low > high:
            return -1
        mid = (low + high) // 2
        if nums[mid] > target:
            return self.binary_search_last(low, mid - 1, nums, target)
        elif nums[mid] < target:
            return self.binary_search_last(mid + 1, high, nums, target)
        else:
            mid1 = self.binary_search_last(mid + 1, high, nums, target)

            if mid1 == -1:
                return mid
            else:
                return mid1

    def search(self, low: int, high: int, nums: list[int], target: int) -> list[int]:

        first = self.binary_search_first(low, high, nums, target)
        last = self.binary_search_last(low, high, nums, target)
        return [first, last]


if __name__ == "__main__":

    solution = Solution()
    nums = [1, 3, 5, 5, 5, 5, 67, 123, 125]
    low = 0
    high = len(nums) - 1
    target = 5
    result = solution.search(low, high, nums, target)
    print(result)

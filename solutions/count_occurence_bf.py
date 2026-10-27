class Solution:
    def binary_search_first_occurence(
        self, low: int, high: int, nums: list[int], target: int
    ) -> int:
        if low > high:
            return -1

        mid = (low + high) // 2

        if nums[mid] > target:
            return self.binary_search_first_occurence(low, mid - 1, nums, target)
        elif nums[mid] < target:
            return self.binary_search_first_occurence(mid + 1, high, nums, target)
        else:
            mid1 = self.binary_search_first_occurence(low, mid - 1, nums, target)

            if mid1 == -1:
                return mid
            else:
                return mid1

    def binary_search_last_occurence(
        self, low: int, high: int, nums: list[int], target: int
    ) -> int:
        if low > high:
            return -1

        mid = (low + high) // 2

        if nums[mid] > target:
            return self.binary_search_last_occurence(low, mid - 1, nums, target)
        elif nums[mid] < target:
            return self.binary_search_last_occurence(mid + 1, high, nums, target)
        else:
            mid1 = self.binary_search_last_occurence(mid + 1, high, nums, target)

            if mid1 == -1:
                return mid
            else:
                return mid1

    def search(self, low: int, high: int, nums: list[int], target: int) -> int:
        first_occ = self.binary_search_first_occurence(low, high, nums, target)
        if first_occ == -1:
            return 0
        else:
            last_occ = self.binary_search_last_occurence(low, high, nums, target)
            return (last_occ - first_occ) + 1


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 3, 5, 5, 5, 5, 67, 123, 125]
    low = 0
    high = len(nums) - 1
    target = 5
    result = solution.search(low, high, nums, target)
    print(result)

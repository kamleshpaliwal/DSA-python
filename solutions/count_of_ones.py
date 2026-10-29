class Solution:
    def binary_first_occ_of_one(
        self, low: int, high: int, nums: list[int], target: int
    ) -> int:
        if low > high:
            return -1

        mid = (low + high) // 2
        if nums[mid] > target:
            return self.binary_first_occ_of_one(low, mid - 1, nums, target)
        elif nums[mid] < target:
            return self.binary_first_occ_of_one(mid + 1, high, nums, target)
        else:
            mid1 = self.binary_first_occ_of_one(low, mid - 1, nums, target)

            if mid1 == -1:
                return mid
            else:
                return mid1

    def count_of_ones(self, low: int, high: int, nums: list[int], target: int) -> int:
        first_occ_of_one = self.binary_first_occ_of_one(low, high, nums, target)
        count_of_ones = len(nums) - first_occ_of_one
        return count_of_ones


if __name__ == "__main__":
    solution = Solution()
    nums = [0, 0, 0, 1, 1, 1]
    low = 0
    high = len(nums) - 1
    target = 1
    result = solution.count_of_ones(low, high, nums, target)
    print(result)

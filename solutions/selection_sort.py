class Solution:
    @classmethod
    def selection_sort(self, nums: list[int]) -> list[int]:
        n = len(nums)
        for i in range(n - 1):
            min_ind = i
            for j in range(i + 1, n):
                if nums[j] < nums[min_ind]:
                    min_ind = j
            nums[i], nums[min_ind] = nums[min_ind], nums[i]

        return nums


if __name__ == "__main__":
    nums = [1, 3, 2]
    result = Solution.selection_sort(nums)
    print("result", result)

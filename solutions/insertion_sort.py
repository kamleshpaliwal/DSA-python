class Solution:
    @classmethod
    def insertion_sort(self, nums: list[int]) -> list[int]:
        n = len(nums)
        for i in range(1, n):
            x = nums[i]
            j = i - 1
            while j >= 0 and x < nums[j]:
                nums[j + 1] = nums[j]
                j = j - 1
            nums[j + 1] = x
        return nums


if __name__ == "__main__":
    nums = [1, 4, 3]
    result = Solution.insertion_sort(nums)
    print("result", result)

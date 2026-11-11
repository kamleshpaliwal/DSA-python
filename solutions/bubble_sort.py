class Solution:
    @classmethod
    def bubble_sort(self, nums: list[int]) -> list[int]:
        len_of_nums = len(nums)
        for i in range(len_of_nums):
            swapped = False
            for j in range(len_of_nums - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swapped = True
            if swapped == False:
                return nums
        return nums


if __name__ == "__main__":
    nums = [1, 4, 3, 20, 10, 30, 15]
    result = Solution.bubble_sort(nums)
    print("result", result)

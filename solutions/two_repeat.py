class Solution:
    def two_repeat(self, nums: list[int], n: int) -> list[int]:
        result_arr = []
        for i in range(n + 2):
            absv = abs(nums[i])
            if nums[absv] > 0:
                nums[absv] = -nums[absv]
            else:
                result_arr.append(absv)

        return result_arr


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 1, 2]
    result = solution.two_repeat(nums, 3)
    print(result)

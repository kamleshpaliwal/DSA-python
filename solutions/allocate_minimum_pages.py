class Solution:
    def min_pages(self, nums: list[int], n: int, k: int) -> int:
        if k == 1:
            return sum(nums[0:n])
        if n == 1:
            return nums[0]
        res = float("inf")
        for i in range(1, n):
            res = min(res, max(self.min_pages(nums, i, k - 1), sum(nums[i:n])))

        return res


if __name__ == "__main__":
    solution = Solution()
    nums = [10, 20, 30]
    k = 2
    result = solution.min_pages(nums, len(nums), k)
    print(result)

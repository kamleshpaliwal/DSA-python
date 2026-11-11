class Solution:
    def is_feasible(self, nums: list[int], n: int, k: int, ans: int) -> bool:
        req, s = 1, 0
        for i in range(n):
            if s + nums[i] > ans:
                req = req + 1
                s = nums[i]
            else:
                s = s + nums[i]
        return req <= k

    def min_pages(self, nums: list[int], k: int) -> int:
        n = len(nums)
        sum_of_array = sum(nums)
        max_of_array = max(nums)
        low, high = max_of_array, sum_of_array
        res = 0
        while low <= high:
            mid = (low + high) // 2
            if self.is_feasible(nums, n, k, mid):
                res = mid
                high = mid - 1
            else:
                low = mid + 1

        return res


if __name__ == "__main__":
    solution = Solution()
    nums = [10, 20, 30]
    k = 2
    result = solution.min_pages(nums, k)
    print("result", result)

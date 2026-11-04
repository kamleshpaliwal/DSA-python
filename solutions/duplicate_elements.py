class Solution:
    def find_duplicates(self, nums: list[int]) -> list[int]:
        res = []
        mp = {}
        length = len(nums)
        for i in range(length):
            mp[nums[i]] = mp.get(nums[i], 0) + 1

            if mp[nums[i]] == 2:
                res.append(nums[i])

        return res


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 3, 1, 4, 3]
    result = solution.find_duplicates(nums)
    print(result)

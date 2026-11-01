class Solution:
    def search(self, low: int, high: int, target: int, nums: list[int]) -> bool:
        found = False
        while low <= high:

            mid = (low + high) // 2

            if nums[mid] == target:
                found = True
                break

            while (low < mid) and (nums[mid] == nums[low]):
                low = low + 1

            while (high > mid) and (nums[mid] == nums[low]):
                low = low + 1

            if nums[mid] <= nums[high]:
                # todo
                if nums[mid] > target:
                    high = mid - 1
                else:
                    if nums[high] < target:
                        high = mid - 1
                    else:
                        low = mid + 1
            else:
                if nums[mid] < target:
                    low = mid + 1
                else:
                    if nums[high] >= target:
                        high = mid - 1
                    else:
                        low = mid + 1

        return found


if __name__ == "__main__":
    solution = Solution()
    nums = [4, 5, 8, 1, 1, 1, 2]
    low = 0
    high = len(nums) - 1
    target = 6
    result = solution.search(low, high, target, nums)
    print(result)

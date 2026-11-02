class Solution:
    def isPairSum(
        self, nums: list[int], target: int, start_index: int, end_index: int
    ) -> bool:
        while start_index < end_index:
            if (nums[start_index] + nums[end_index]) == target:
                return True
            elif (nums[start_index] + nums[end_index]) > target:
                end_index = end_index - 1
            else:
                start_index = start_index + 1

        return False

    def findTriplet(self, nums: list[int], target: int) -> bool:
        end_index = len(nums) - 1
        foundPairSum = False
        for i in range(len(nums) - 2):
            pairTarget = target - nums[i]
            foundPairSum = self.isPairSum(nums, pairTarget, i + 1, end_index)
            if foundPairSum:
                break

        return foundPairSum


if __name__ == "__main__":
    solution = Solution()
    nums = [2, 5, 10, 15, 18]
    target = 43
    result = solution.findTriplet(nums, target)
    print("result", result)

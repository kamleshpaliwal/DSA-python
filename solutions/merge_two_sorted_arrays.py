class Solution:
    @classmethod
    def merge_lists(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result_arr = []
        m = len(nums1)
        n = len(nums2)
        i, j = 0, 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                result_arr.append(nums1[i])
                i = i + 1
            else:
                result_arr.append(nums2[j])
                j = j + 1

        while i < m:
            result_arr.append(nums1[i])
            i += 1

        while j < n:
            result_arr.append(nums2[j])
            j += 1

        return result_arr


if __name__ == "__main__":
    nums1 = [3, 6, 8]
    nums2 = [1, 2, 4, 5]
    result = Solution.merge_lists(nums1, nums2)
    print("result", result)

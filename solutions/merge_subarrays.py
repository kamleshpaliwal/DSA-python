class Solution:
    @classmethod
    def merge_lists(
        self, arr: list[int], nums1: list[int], nums2: list[int], low: int
    ) -> list[int]:
        m = len(nums1)
        n = len(nums2)
        i = 0
        j = 0
        k = low

        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                arr[k] = nums1[i]
                i = i + 1
                k += 1
            else:
                arr[k] = nums2[j]
                j = j + 1
                k += 1

        while i < m:
            arr[k] = nums1[i]
            i += 1
            k += 1

        while j < n:
            arr[k] = nums2[j]
            j += 1
            k += 1

        return arr


if __name__ == "__main__":
    arr = [10, 15, 20, 40, 8, 11, 11]
    low = 0
    high = 6
    mid = 3
    result = Solution.merge_lists(arr, arr[low : mid + 1], arr[mid + 1 : high + 1], low)
    print("result", result)

class Solution:
    @classmethod
    def merge(self, arr: list[int], low, high, mid):
        nums1 = arr[low : mid + 1]
        nums2 = arr[mid + 1 : high + 1]

        m = len(nums1)
        n = len(nums2)

        i = 0
        j = 0
        k = low

        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                arr[k] = nums1[i]
                i = i + 1
                k = k + 1
            else:
                arr[k] = nums2[j]
                j = j + 1
                k = k + 1

        while i < m:
            arr[k] = nums1[i]
            i = i + 1
            k = k + 1

        while j < n:
            arr[k] = nums2[j]
            j = j + 1
            k = k + 1

    @classmethod
    def merge_sort(self, arr: list[int], low: int, high: int):

        if high > low:
            mid = (low + high) // 2
            self.merge_sort(arr, low, mid)
            self.merge_sort(arr, mid + 1, high)
            self.merge(arr, low, high, mid)


if __name__ == "__main__":
    arr = [10, 5, 30, 15, 7]
    low = 0
    high = len(arr) - 1
    Solution.merge_sort(arr, low, high)
    print("result", arr)

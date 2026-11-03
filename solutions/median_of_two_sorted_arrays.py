class Solution:
    def find_median(self, nums1: list[int], nums2: list[int]) -> float | None:
        len1, len2 = len(nums1), len(nums2)
        if len1 > len2:
            nums1, nums2 = nums2, nums1
            len1, len2 = len2, len1

        start_index_1 = 0
        end_index_1 = len1

        while start_index_1 <= end_index_1:
            n1 = (start_index_1 + end_index_1) // 2
            n2 = (len1 + len2 + 1) // 2 - n1

            min1 = float("inf") if n1 == len1 else nums1[n1]
            max1 = float("-inf") if n1 == 0 else nums1[n1 - 1]
            min2 = float("inf") if n2 == len2 else nums2[n2]
            max2 = float("-inf") if n2 == 0 else nums2[n2 - 1]

            if (max1 <= min2) and (max2 <= min1):
                if (len1 + len2) % 2 == 0:
                    return (max(max1, max2) + min(min1, min2)) / 2
                else:
                    return max(max1, max2)
            elif max1 > min2:
                end_index_1 = n1 - 1
            else:
                start_index_1 = n1 + 1

        return None


if __name__ == "__main__":
    solution = Solution()
    a1 = [10, 20, 30]
    a2 = [5, 15, 25, 35, 45]
    result = solution.find_median(a1, a2)
    print("result", result)

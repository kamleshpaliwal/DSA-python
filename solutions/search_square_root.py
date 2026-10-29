class Solution:
    def search_square_root(self, num: int) -> int:
        low = 0
        high = num - 1
        answer = 0

        while low <= high:
            mid = (low + high) // 2
            print(mid)
            if (mid * mid) > num:
                high = mid - 1
            else:
                if (mid * mid) <= num:
                    low = mid + 1
                    answer = mid

        return answer


if __name__ == "__main__":
    solution = Solution()
    result = solution.search_square_root(45)
    print("answer", result)

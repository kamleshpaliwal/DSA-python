class Solution:
    @classmethod
    def reverse(self, str1: str, start: int, end: int):
        i, j = start, end
        while i < j:
            str1[i], str1[j] = str1[j], str1[i]
            i += 1
            j -= 1

    @classmethod
    def string_of_words(self, str1):
        str1 = list(str1)
        n = len(str1)
        i = 0
        s = 0
        while i < n:
            if str1[i] == " ":
                Solution.reverse(str1, s, i - 1)
                s = i + 1
            i = i + 1

        Solution.reverse(str1, s, n - 1)
        Solution.reverse(str1, 0, n - 1)

        return "".join(str1)


if __name__ == "__main__":
    str1 = "India is Great"
    result = Solution.string_of_words(str1)
    print("result", result)

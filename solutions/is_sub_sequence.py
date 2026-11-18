class Solution:
    @classmethod
    def is_sub_seq(self, str1: str, str2: str) -> bool:
        i, j = 0, 0
        while i < len(str1) and j < len(str2):
            if str1[i].lower() == str2[j].lower():
                i += 1
                j += 1
            else:
                i += 1

        return j == len(str2)


if __name__ == "__main__":
    str1 = "ABCD"
    str2 = "Ac"
    result = Solution.is_sub_seq(str1, str2)
    print("result", result)

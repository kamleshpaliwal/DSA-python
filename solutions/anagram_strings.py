class Solution:
    @classmethod
    def is_anagram(self, str1: str, str2: str) -> bool:
        m = len(str1)
        n = len(str2)
        if m != n:
            return False

        count = [0] * 256
        for i in range(m):
            count[ord(str1[i])] += 1
            count[ord(str2[i])] += 1

        for x in range(len(count)):
            if count[x] == 1:
                return False

        return True


if __name__ == "__main__":
    result = Solution.is_anagram("kam", "man")
    print("result", result)

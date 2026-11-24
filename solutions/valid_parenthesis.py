class Solution:
    @classmethod
    def valid_parenthesis(self, string_par: str) -> bool:
        stack = []
        pair = {")": "(", "]": "[", "{": "}"}

        for char in string_par:
            if pair.get(char):
                if not stack or stack[-1] != pair.get(char):
                    return False
                else:
                    stack.pop()

            else:
                stack.append(char)

        return len(stack) == 0


if __name__ == "__main__":
    result = Solution.valid_parenthesis("[])")
    print(result)

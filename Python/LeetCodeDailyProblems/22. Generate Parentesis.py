from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(left, right, s):

            if len(s) == n * 2:
                res.append(s)
                return

            if left < n:
                dfs(left + 1, right, s + '(')

            if right < left:
                dfs(left, right + 1, s + ')')
            print(res)

        res = []
        dfs(0, 0, '')
        return res

def count_frequency(numbers):
    frequency = {}
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            breakpoint()
            frequency[num] = 1
    return frequency

# Test the function
nums = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
frequency_count = count_frequency(nums)
print(frequency_count)

if __name__ == '__main__':
    n = 3
    print(Solution().generateParenthesis(n))
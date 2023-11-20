# https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/

class Solution:
    def countSmaller(self, nums):
        def merge_sort(enum):
            if len(enum) <= 1:
                return enum

            mid = len(enum) // 2
            left, right = merge_sort(enum[:mid]), merge_sort(enum[mid:])

            for i in range(len(enum) - 1, -1, -1):
                if not right or (left and left[-1][1] > right[-1][1]):
                    result[left[-1][0]] += len(right)
                    enum[i] = left.pop()
                else:
                    enum[i] = right.pop()

            return enum

        result = [0] * len(nums)
        merge_sort(list(enumerate(nums, start=0)))

        return result

solution = Solution()
nums = [5, 2, 6, 1]
output = solution.countSmaller(nums)
print(output)

class Solution:
    def subsets(self, nums):
        result = []
        subset = []

        def backtrack(i):
            if i == len(nums):
                result.append(subset.copy())
                return

            # Cogemos nums[i]
            subset.append(nums[i])
            backtrack(i + 1)

            # No cogemos nums[i]
            subset.pop()
            backtrack(i + 1)

        backtrack(0)

        return result
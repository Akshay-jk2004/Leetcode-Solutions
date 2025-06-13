class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(remaining, combo, start):
            if remaining == 0:
                result.append(list(combo))  # Found valid combination
                return
            elif remaining < 0:
                return  # Exceeded the sum, backtrack

            for i in range(start, len(candidates)):
                combo.append(candidates[i])             # Choose the candidate
                backtrack(remaining - candidates[i], combo, i)  # Not i+1 because we can reuse the same element
                combo.pop()                             # Undo the choice

        backtrack(target, [], 0)
        return result

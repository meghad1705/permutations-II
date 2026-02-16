class Solution(object):
    def permuteUnique(self, nums):
        nums.sort()                     # Step 1: Sort the array
        result = []
        used = [False] * len(nums)      # Track used elements

        def backtrack(path):
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            for i in range(len(nums)):
                # Skip used elements
                if used[i]:
                    continue
                
                # Skip duplicates
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                
                used[i] = True
                path.append(nums[i])
                
                backtrack(path)
                
                # Backtrack
                path.pop()
                used[i] = False

        backtrack([])
        return result

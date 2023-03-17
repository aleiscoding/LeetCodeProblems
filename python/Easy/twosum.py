class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute force : O(N^2)
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # Optimized using Hash Maps : O(N)
        hashNum = {}
        for i in range(len(nums)):
            if target - nums[i] in hashNum:
                return [hashNum[target - nums[i]], i]
            hashNum[nums[i]] = i
        return []

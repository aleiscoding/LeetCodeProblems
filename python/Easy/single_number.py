def singleNumber(self, nums: List[int]) -> int:
        # Both solutions are O(n)
        # One-liner
        return 2 * sum(set(nums)) - sum(nums)

        # Hash solution
        # hashSet = {}

        for num in nums:
            if num not in hashSet:
                hashSet[num] = 1
            else:
                hashSet[num] += 1

        for num in nums:
            if hashSet[num] == 1:
                return num

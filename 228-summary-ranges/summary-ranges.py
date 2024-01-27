class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        res = []
        i = 0
        while i < len(nums):
            j = i
            while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1:
                j += 1

            if i == j:
                res.append(f"{nums[i]}")
            else:
                res.append(f"{nums[i]}->{nums[j]}")

            i = j + 1

        return res

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hm = {}
        for i in range(len(nums)):
            if target - nums[i] in hm:
                return [hm[target - nums[i]], i]
            hm[nums[i]] = i
        return []


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([3, 2, 4], 6))

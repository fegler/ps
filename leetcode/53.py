class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ret = nums[0]
        now = nums[0]
        for i in range(1, len(nums)):
            now = max(now+nums[i], nums[i])
            max_ret = max(max_ret, now)
        return max_ret
        # def recur(nums, left, right):
        #     if left > right:
        #         return -100000
        #     mid = (left+right)//2 
        #     now, l_sum, r_sum = 0, 0, 0
        #     for i in range(mid-1, left-1, -1):
        #         now += nums[i]
        #         l_sum = max(l_sum, now)
        #     now = 0 
        #     for i in range(mid+1, right+1):
        #         now += nums[i]
        #         r_sum = max(r_sum, now)
        #     total_max = nums[mid] + l_sum + r_sum

        #     left_max = recur(nums, left, mid-1)
        #     right_max = recur(nums, mid+1, right)

        #     return max(total_max, left_max, right_max)

        # return recur(nums, 0, len(nums)-1)
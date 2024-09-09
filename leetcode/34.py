class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1
        if len(nums) == 0:
            return [-1, -1]
        while left <= right:
            mid_idx = (left+right)//2
            l, r, mid = nums[left], nums[right], nums[mid_idx]
            if mid == target:
                ret_l, ret_r = mid_idx, mid_idx 
                for i in range(1, len(nums)):
                    flag = True
                    if ret_l >=1 and nums[ret_l-1]==target:
                        ret_l -= 1
                        flag = False 
                    if ret_r < len(nums)-1 and nums[ret_r+1]==target:
                        ret_r += 1 
                        flag = False 
                    if flag:
                        break
                return [ret_l, ret_r]

            if l == r:
                return [-1, -1]
            if mid < target:
                left = mid_idx + 1 
            else:
                right = mid_idx -1
             
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid_idx = (left+right)//2
            l, r, mid = nums[left], nums[right], nums[mid_idx]
            if mid == target:
                return mid_idx 

            if l == r:
                return -1
            
            if l > r:
                ## rotated 
                if mid > r:
                    ## k ~ N
                    if target < l:
                        left = mid_idx + 1 
                        continue 
                else:
                    ## 1 ~ k-1
                    if target > r:
                        right = mid_idx - 1
                        continue 
            
            ## original binary search 
            if mid > target:
                right = mid_idx - 1
            else:
                left = mid_idx + 1 
        return -1 
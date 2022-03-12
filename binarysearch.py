class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first_idx=0
        last_idx=len(nums)-1
        while last_idx>=first_idx:
            mid=(first_idx+last_idx)//2
            if target== nums[mid]:
                return mid
                break
            elif target<nums[mid]:
                last_idx=mid-1
            else:
                first_idx=mid+1
        if first_idx>last_idx:
            return -1
        
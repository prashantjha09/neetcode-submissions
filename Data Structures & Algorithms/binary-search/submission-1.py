class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)-1
        mid = int((j-i) / 2)
        while j>=i:
            mid = int((j + i) / 2)
            if nums[mid] == target :
                return mid
            elif nums[mid] > target:
                j = mid-1
            else:
                i = mid+1
        return -1
        
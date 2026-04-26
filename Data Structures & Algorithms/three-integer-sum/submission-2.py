class Solution:
    def __init__(self):
        self.output = []
    def two_sum(self, nums: list[int], k, start_point):
        i = start_point
        j = len(nums) - 1
        while i < j:
            if nums[i] + nums[j] + k > 0:
                j -= 1
            elif nums[i] + nums[j] + k < 0:
                i += 1
            else:
                self.output.append([k, nums[i], nums[j]])
                i += 1
                j -= 1

                while i < j and nums[i] == nums[i-1]:
                    i += 1
                while i < j and nums[j] == nums[j+1]:
                    j -= 1



    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.two_sum(nums, nums[i], i+1 )
        return self.output


        
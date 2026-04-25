class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        order = defaultdict(list)
        for i, index in enumerate(nums):
            order[index].append(i)
        nums = sorted(nums)
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] + nums[j] > target:
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                first_index = order[nums[i]][0]
                del order[nums[i]][0]

                second_index = order[nums[j]][0]
                del order[nums[j]][0]

                return sorted([first_index, second_index])

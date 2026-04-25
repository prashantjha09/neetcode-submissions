class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_len = defaultdict(int)
        max_output = 0
        tmp_output = 0
        for i in nums:
            if i-1 in max_len:
                max_len[i] = max_len[i-1]-1
                tmp_output = max_len[i-1]-1
            elif i+1 in max_len:
                max_len[i] = max_len[i+1] + 1
                tmp_output = max_len[i+1]+1
            else:
                count = 1
                tmp_i = i
                while i+1 in nums:
                    count+=1
                    i+=1
                max_len[tmp_i] = count
                tmp_output = count
                max_output= max(max_output, tmp_output)

        return max(tmp_output,max_output)

class Solution:
    def __init__(self):
        self.count_char = defaultdict(int)    
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = len(s)
        if max_len == 0:
            return 0
        left = 0
        right = 0
        self.count_char[s[right]]= 1
        max_substring_len = 1
        while right >= left and right < max_len-1:
            if self.count_char.get(s[right+1], 0)==0:
                right+=1
                self.count_char[s[right]] = 1
            else:
                self.count_char[s[left]] =  self.count_char[s[left]]-1
                left += 1
                self.count_char[s[left]] = 1
                if right < left:
                    right = left
            max_substring_len = max(max_substring_len, right-left+1)
        return  max_substring_len



        
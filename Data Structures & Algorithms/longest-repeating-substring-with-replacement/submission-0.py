from collections import defaultdict


class Solution:
    def check_change_required(self, char_count_dic):
        max_count = -float("inf")
        for i in char_count_dic:
            max_count = max(max_count, char_count_dic[i])

        return max_count

    def characterReplacement(self, s: str, k: int):
        i = 0
        j = 0
        char_count = defaultdict(int)
        max_len = 0  

        while len(s) > j >= i:

            char_count[s[j]] = char_count[s[j]] + 1
            max_count = self.check_change_required(char_count)
            total_char = j - i + 1

            if (total_char - max_count) <= k:
                max_len = max(max_len, total_char) 
                j += 1

            else:
                char_count[s[i]] = char_count[s[i]] - 1
                i += 1
                j += 1


        return max_len  

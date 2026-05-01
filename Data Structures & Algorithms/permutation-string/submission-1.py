class Solution:
    def check_count(self,count_dict, s1_count_dict):    
        for i in count_dict:
            if count_dict[i]!=s1_count_dict[i]:
                return False
        return True
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)

        s1_count_dict = {char: 0 for char in s1}
        for char in s1:
            s1_count_dict[char] += 1

        count_dict = {element:0 for element in s1}

        s1_set = set(s1)

        i = 0
        j = 0


        while j < len(s2):

            if s2[j] in s1_set:
                count_dict[s2[j]] += 1


            if j-i == s1_len-1:
                if self.check_count(count_dict, s1_count_dict):
                    return True

                if s2[i] in s1_set:
                    count_dict[s2[i]] -= 1
                i += 1
            j+=1

        return False

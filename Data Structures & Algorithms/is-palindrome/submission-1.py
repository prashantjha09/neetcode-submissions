class Solution:
    def isPalindrome(self, s: str) -> bool:
        allowed = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        s = s.replace(" ", "")
        i = 0
        j = len(s) - 1
        while i <= j:
            if s[i].lower() not in allowed:
                i+=1
            if s[j].lower() not in allowed:
                j -= 1
            else:
                if  s[i].lower() != s[j].lower():
                    return False
                i += 1
                j -= 1
        return True
        
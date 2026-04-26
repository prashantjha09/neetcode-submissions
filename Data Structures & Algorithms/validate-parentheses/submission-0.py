class Solution:
    def isValid(self, s: str) -> bool:
        pair_dict = { "}":"{", "]":"[", ")":"(" }
        stack = deque()
        for i in s:
            if i in pair_dict.values():
                print(f"into if {i}")
                stack.append(i)
            else:
                if not stack:
                    return False
                val = stack.pop()
                if val != pair_dict[i]:
                    return False
        print(stack)
        return True if not stack else False
        
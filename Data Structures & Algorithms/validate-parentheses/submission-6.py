# import queue
from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        seen = deque()
        valid = False
        for c in s:
            if c in '[({':
                # print("c is: ", c)
                seen.append(c)
            elif c in '])}':
            #  and len(seen) > 0:
                if not seen:
                    return False
                if c == ']':
                    valid = (seen.pop() == '[')
                    # print("valid: ", valid)
                    if not valid:
                        return False
                if c == ')':
                    valid = (seen.pop() == '(')
                    # print("valid: ", valid)
                    if not valid:
                        return False
                if c == '}':
                    valid = (seen.pop() == '{')
                    # print("valid: ", valid)
                    if not valid:
                        return False
        return len(seen) == 0
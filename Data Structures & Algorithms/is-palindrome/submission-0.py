class Solution:
    def isPalindrome(self, s: str) -> bool:
        print("s: ", s)
        s = s.replace(" ", "").lower()
        print("s: ", s)
        filtered_s = "".join(char for char in s if char.isalpha())
        print("filtered_s: ", filtered_s)
        # start = 0
        # end = len(filtered_s) - 1
        s_len = len(filtered_s)
        for i in range(len(filtered_s)):
            if filtered_s[i] != filtered_s[s_len-i-1]:
                return False
        return True
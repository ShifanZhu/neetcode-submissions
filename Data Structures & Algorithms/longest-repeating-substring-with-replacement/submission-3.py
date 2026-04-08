class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0  # left pointer of sliding window

        max_len = 0   # stores the maximum valid window length found so far
        max_freq = 0  # highest frequency of a single character in current window

        freq = defaultdict(int)  # frequency map for characters in current window

        # expand the window using right pointer r
        for r, c in enumerate(s):
            # include current character into the window
            freq[c] += 1

            # update the max frequency of any single character in the window
            # this helps us know how many replacements are needed
            max_freq = max(max_freq, freq[c])

            # check if current window is invalid:
            # total chars to replace = window size - most frequent char count
            # if this exceeds k, we need to shrink the window
            while (r - l + 1) - max_freq > k:
                # remove the leftmost character from the window
                freq[s[l]] -= 1
                l += 1  # shrink window from the left

            # at this point, window is valid
            # update the maximum length
            max_len = max(max_len, r - l + 1)

        return max_len
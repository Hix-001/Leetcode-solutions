# 02/08/2026
# Hard
# LeetCode 76: Minimum Window Substring using a sliding window and frequency maps.
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        count_t = {}
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1
        window = {}
        have, need = 0, len(count_t)
        res, res_len = [-1, -1], float("infinity")
        left = 0
        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1
            if char in count_t and window[char] == count_t[char]:
                have += 1
            while have == need:
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1
                left_char = s[left]
                window[left_char] -= 1
                if left_char in count_t and window[left_char] < count_t[left_char]:
                    have -= 1
                left += 1
        l, r = res
        return s[l:r+1] if res_len != float("infinity") else ""
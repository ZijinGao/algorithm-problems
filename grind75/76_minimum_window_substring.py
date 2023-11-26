from collections import deque, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''
        if s == t:
            return s
        
        latest_idx = {}
        t_char_count = defaultdict(int)
        for char in t:
            latest_idx[char] = deque()
            t_char_count[char] += 1        
        total_apperance_count = 0
        min_length = float('inf')
        out = ''
        for idx, char in enumerate(s):
            print(idx, char)
            if char in latest_idx:
                latest_idx[char].append(idx)
                total_apperance_count += 1
                if len(latest_idx[char]) > t_char_count[char]:
                    latest_idx[char].popleft()
                    total_apperance_count -= 1
                if total_apperance_count < len(t): continue
                earliest_idx = float('inf')
                for _char in latest_idx.keys():
                    earliest_idx = min(earliest_idx, latest_idx[_char][0])
                curr_length = idx - earliest_idx + 1
                if curr_length < min_length:
                    min_length = curr_length
                    out = s[earliest_idx: idx+1]
        return out
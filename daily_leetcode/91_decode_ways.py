class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        new_array = []
        for num in s:
            if num != "0":
                new_array.append(num)
            else:
                last = new_array.pop()
                new_array.append(last+num)

        for num in new_array:
            if int(num) > 26:
                return 0

        dp = [0 for _ in range(len(new_array))]
        dp[0] = 1

        if len(new_array) == 1:
            return 1
        if int(new_array[0] + new_array[1]) <=26:
            dp[1] = 2
        else:
            dp[1] = 1
        
        for i in range(2, len(new_array)):
            dp[i] = dp[i - 1]
            if int(new_array[i-1]+new_array[i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[-1]
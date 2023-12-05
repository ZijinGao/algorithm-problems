class Solution:
    def numberOfMatches(self, n: int) -> int:
        curr_teams = n
        total = 0
        while curr_teams > 1:
            if curr_teams % 2 == 1:
                total += (curr_teams - 1) / 2
                curr_teams = (curr_teams - 1) / 2 + 1
            else:
                total += curr_teams / 2
                curr_teams /= 2

        return int(total)
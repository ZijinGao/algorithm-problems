from collections import defaultdict
class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        lost = defaultdict(int)
        all_players = {matches[0][0]}
        for pair in matches:
            lost[pair[1]] += 1
            all_players.add(pair[0])
            all_players.add(pair[1])


        never_lost = []
        lost_once = []
        for player in all_players:
            if not lost.get(player, None):
                never_lost.append(player)
            elif lost.get(player, None) == 1:
                lost_once.append(player)
        
        never_lost.sort()
        lost_once.sort()
        return [never_lost, lost_once]
        
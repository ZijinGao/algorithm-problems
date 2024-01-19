from collections import defaultdict
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:

        table = defaultdict(int)
        for t in tasks:
            table[t] += 1
        max_count = max(list(table.values()))
        max_letters = 0
        for key, val in table.items():
            if val == max_count:
                max_letters += 1

        return max((max_count - 1) * (n+1) + max_letters, len(tasks))
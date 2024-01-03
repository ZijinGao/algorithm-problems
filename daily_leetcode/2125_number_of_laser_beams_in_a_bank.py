class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        count = []
        total = 0
        for idx, row in enumerate(bank):
            bank[idx] = list(map(int, list(row)))

        for row in bank:
            if sum(row) != 0:
                count.append(sum(row))

        for i in range(len(count) - 1):
            total += count[i] * count[i+1]
        return total

from collections import defaultdict
class SQL:
    def __init__(self, names: list[str], columns: list[int]):
        self.data = defaultdict(dict)
        self.rowIndexes = {name: 0 for name in names}
        
    def insertRow(self, name: str, row: list[str]) -> None:
        self.rowIndexes[name] += 1
        self.data[name][self.rowIndexes[name]] = row

    def deleteRow(self, name: str, rowId: int) -> None:
        del self.data[name][rowId]

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        return self.data[name][rowId][columnId-1]
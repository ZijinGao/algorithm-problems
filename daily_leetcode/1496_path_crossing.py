class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()
        visited.add(tuple([0,0]))
        position = [0,0]
        directions = {
            "N": [0,1],
            "E": [1,0],
            "W": [-1,0],
            "S": [0,-1]
        }
        for letter in path:
            position[0] += directions[letter][0]
            position[1] += directions[letter][1]
            new_position = tuple(position)
            if new_position in visited:
                return True
            visited.add(new_position)

        return False
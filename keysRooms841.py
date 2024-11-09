

def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(rooms: List[List[int]], currentRoomIdx, visited):
            for room in rooms[currentRoomIdx]:
                if room not in visited:
                    visited.add(room)
                    dfs(rooms, room, visited)
        visited = {0}
        dfs(rooms, 0, visited)
        return len(visited) == len(rooms)
"""
rooms[0] is unlocked at the start
pick up keys starting at [0]
for each room, check if we have its key
keys = []
New approach:
Start from 0, go to the rooms to which its keys belong
Check if all rooms were visited, using a set. If len(set) != len(rooms), return false
graph DFS? go down the list i guess
start with rooms[0]
def dfs(rooms: List[List[int]], currentRoomIdx, visited):
    for room in rooms[currentRoomIdx]:
        if room not in visited:
            visited += room
            dfs(rooms, room, visited)
        if room in visited:
            do nun
visited = []
visited += dfs(rooms, 0, visited)
return len(visited) == len(rooms)
"""


def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = []
        for i in range(len(rooms)):
            if i == 0:
                seen.append(True)
            else:
                seen.append(False)
        keyQueue = [0]
        while len(keyQueue) > 0:
            currentKey = keyQueue.pop(0)
            for newKey in rooms[currentKey]:
                if seen[newKey] == False:
                    seen[newKey] = True
                    keyQueue.append(newKey)
        
        for myBool in seen:
            if not myBool:
                return False
        return True
"""
seen = false list, first is true
queue = [0]
while there are keys in the queue:
    current key is queue pop 0
    for each new key in rooms[current key]:
        check seen[new key] as true, since we'll "visit", moreso check as visited
        append new key to queue, so that we can then see what keys it has
"""



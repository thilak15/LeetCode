class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        # Any element can have only two adjacent elements exepet the first and last
        adj = defaultdict(list)
        for a, b in adjacentPairs:
            adj[a].append(b)
            adj[b].append(a)
        # Find the start element (The start element will have only one adjacent element by  chekcing length each value in the dict we can find the start element)
        for x, y in adj.items():
            if len(y) == 1:
                start = x
                break
        print(adj)
        res=[]
        visited=set()
        while start is not None:
            res.append(start)
            visited.add(start)
            next_element=[x for x in adj[start] if x not in visited]
            start = next_element[0] if next_element else None

        return res
    # Time complexity O(n)
    # space Complexity O(n)


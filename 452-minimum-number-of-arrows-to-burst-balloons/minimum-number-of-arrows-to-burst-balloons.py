class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x:x[0])

        merged=[]

        for i in points:
            if not merged or merged[-1][1]<i[0]:
                merged.append(i)
            else:
                merged[-1][1]=min(merged[-1][1],i[1])
        print(merged)
        return len(merged)
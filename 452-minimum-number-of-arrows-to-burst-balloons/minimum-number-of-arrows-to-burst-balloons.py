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
        return len(merged)
    # This is same as merging intervals sor the array using the first values and merge the intevals only diffrenece is we consider the mnimum value while merging the intrval so that the common point will be there
    # Time complexity O(nlogn)
    # space complexity O(n)
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        """res = []
        max_height = 0
        n = len(heights)
        for i in range(n-1, -1,-1):
            if heights[i] >= max_height:
                res.append(i)
                max_height = heights[i]
        return res[::-1]"""

    # The question gave me the hint to traverse from right to left than left to right
    # Time complexity O(n)
    # space complexit O(n)

    # now using Stack
        stack = []
        n = len(heights)
        for i in range(n):
            while stack and heights[i] >= heights[stack[-1]]:
                stack.pop()
            stack.append(i)
        return stack
    # Time complexity O(n)
    # space Complexity O(n)

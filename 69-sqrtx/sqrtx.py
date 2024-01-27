class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        l, h = 1, x
        while l <= h:
            m = (l + h) // 2
            if m * m == x:
                return m
            elif m * m < x:
                l = m + 1
            else:
                h = m - 1
        return l - 1

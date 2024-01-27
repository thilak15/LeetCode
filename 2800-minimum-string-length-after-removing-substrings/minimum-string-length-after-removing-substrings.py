class Solution:
    def minLength(self, s: str) -> int:

        """stack=[]"""
        # Here i started considering stack data structure cause if i go for the array usew while loop it will be very difficult to track the string and concatenation after removing the substrings

        """for i in s:
            stack.append(i)
            while len(stack)>=2 :
                if str(stack[-2]+stack[-1])=="AB" or str(stack[-2]+stack[-1])=="CD":
                    stack.pop()
                    stack.pop()
                else:
                    break
        return len(stack) """
    # time complexity will be O(n) as the nested while loop will push the each element once
    # space complexity will be  O(n)

    # we can also Slove this problem by taking advantage of the replace function in python

        while "AB" in s or "CD" in s:
            if "AB" in s:
                s=s.replace("AB","")
            if "CD" in s:
                s=s.replace("CD","")
        return len(s)


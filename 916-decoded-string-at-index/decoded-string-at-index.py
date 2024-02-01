class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        size=0
        for i in s:
            if i.isdigit():
                size*=int(i)
            else:
                size+=1
        for c in reversed(s):
            k%=size
            if k==0 and c.isalpha():
                return c
            if c.isdigit():
                size//=int(c)
            else:
                size-=1
        print(k)
# We dont have to form the string we can just keep track of the size o f the string and the traverse from back and retun hte char when k is 0
# Time Complexity O(n)
# Space Complexit O(1)
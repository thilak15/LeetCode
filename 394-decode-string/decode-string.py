class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == '[':
                stack.append(num)
                num = 0
            elif char == ']':
                substr = ''
                while isinstance(stack[-1], str):
                    substr = stack.pop() + substr
                repeat = stack.pop()
                stack.append(substr * repeat)
            else:
                stack.append(char)
        
        return ''.join(stack)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Sort the strings by their length
        strs.sort(key=len)

        # Iterate over each character in the shortest string
        for i in range(len(strs[0])):
            # Compare this character with the corresponding character in all other strings
            for s in strs[1:]:
                if i == len(s) or s[i] != strs[0][i]:
                    # As soon as a mismatch is found, return the prefix up to this point
                    return strs[0][:i]

        # If no mismatch is found, the entire first string is the common prefix
        return strs[0]

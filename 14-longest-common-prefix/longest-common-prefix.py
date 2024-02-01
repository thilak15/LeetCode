class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """if not strs:
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
        return strs[0]"""

        # Time complexity O(n*mlogn)+O(n*m)=O(n*mlogn)
        # Space complexity O(1)

        # we can reduce the time complexity of the above code by just taking out the sorting step
        # consider the first string as the prefix compare it with other strings when ever there is a mismatch reduce the lenght of the prefix to that point
        # This approach Takes down the timecomplexity to O(n*m)
        if not strs:
            return ""
        prefix=strs[0]

        for s in strs:
            while not s.startswith(prefix):
                prefix=prefix[:-1]

                if not prefix:
                    return ""
        return prefix

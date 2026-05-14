#Optimized Approach Tc = O(N * M), Sc = O(1)
def longestCommonPrefix(self, strs):
        
    prefix = strs[0]

    for word in strs[1:]:

        while word[:len(prefix)] != prefix:
            prefix = prefix[:-1]

            if prefix == "":
                return ""

    return prefix
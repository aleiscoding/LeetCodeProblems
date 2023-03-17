def longestCommonPrefix(self, strs: List[str]) -> str:
        # O(S) | O(1)
        lcp = ""
        if not strs:
            return lcp
        
        for i in range(len(strs[0])):
            char = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != char:
                    return lcp
            
            lcp += char

        return lcp 

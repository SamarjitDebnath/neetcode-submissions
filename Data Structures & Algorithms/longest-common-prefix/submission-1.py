class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = float('inf')
        shortest_elem = ""
        for elem in strs:
            if len(elem) < shortest:
                shortest = len(elem)
                shortest_elem = elem
        
        if shortest == 0:
            return ""

        prefix = ""
        for i in range(shortest):
            for elem in strs:
                if elem[i] != shortest_elem[i]:
                    return prefix
            prefix += elem[i]

        return prefix
                
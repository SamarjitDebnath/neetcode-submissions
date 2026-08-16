class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(word)}${word}" for word in strs)

    def decode(self, s: str) -> List[str]:
        if not s: return []

        decoded = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "$":
                j += 1

            word_length = int(s[i:j])
            i = j + 1
            j = i + word_length
            decoded.append(s[i:j])
            i = j

        return decoded
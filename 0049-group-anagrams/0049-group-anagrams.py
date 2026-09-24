class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        h = {}
        for word in strs:
            count = [0]*26
            for ch in word:
                count[ord(ch)- ord('a')]+=1
            key = tuple(count) #because we cant store list as key
            if key not in h:
                h[key] = [word]
            else:
                h[key].append(word)
        return list(h.values())
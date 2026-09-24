class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        h = {}

        for i in strs:
            key = ''.join(sorted(i))

            if key not in h:
                h[key] = [i]
            else:
                h[key].append(i)

        return list(h.values())
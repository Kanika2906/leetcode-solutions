class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping_s2t = {}
        mapping_t2s = {}
        for i in range(0,len(s)):
            if s[i] not in mapping_s2t:
                mapping_s2t[s[i]] = t[i]
            else:
                if mapping_s2t[s[i]]!=t[i]:
                    return False
            if t[i] not in mapping_t2s:
                mapping_t2s[t[i]] = s[i]
            else:
                if mapping_t2s[t[i]]!=s[i]:
                    return False
        return True

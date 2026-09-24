class Solution:
    def reverseVowels(self, st: str) -> str:
        i = 0
        j = len(st)-1
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        s = list(st)
        while j>i:
            if s[i] not in vowels:
                i+=1
                continue
            if s[j] not in vowels:
                j-=1
                continue
            c = s[i]
            s[i] = s[j]
            s[j] = c
            i+=1
            j-=1
        return "".join(s)
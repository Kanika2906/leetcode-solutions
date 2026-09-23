class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        for i in range(0,len(words)):
            start = 0
            c = list(words[i])
            right = len(c)-1
            while right>start:
                c[start],c[right] = c[right],c[start]
                start+=1
                right-=1
            words[i] = "".join(c)
        return " ".join(words)
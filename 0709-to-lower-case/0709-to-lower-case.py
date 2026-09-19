class Solution:
    def toLowerCase(self, s: str) -> str:
        string = ""
        for i in s:
            if 65<=ord(i)<=90:
                string += chr(ord(i)+32)
            else:
                string+=i
        return string
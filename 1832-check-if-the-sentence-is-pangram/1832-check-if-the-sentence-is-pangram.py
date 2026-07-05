class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        ans = True
        for i in range(97,123):
            p=chr(i)
            if p not in sentence:
                ans = False
                break
        return ans

            
        
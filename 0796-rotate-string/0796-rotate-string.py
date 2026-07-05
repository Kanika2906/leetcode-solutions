class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if(len(s)!= len(goal)):
            return False
        else:
            if(s in (goal + goal)):
                return True
            else:
                return False
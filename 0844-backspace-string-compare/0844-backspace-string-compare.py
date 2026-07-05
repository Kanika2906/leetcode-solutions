class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        st=[]
        for ch in list(s):
            if ch=="#":
                if len(st)==0:
                    continue
                else:
                    st.pop()
            else:
                st.append(ch)
        sty=[]
        for ch in list(t):
            if ch=="#":
                if len(sty)==0:
                    continue
                else:
                    sty.pop()
            else:
                sty.append(ch)
        if st==sty:
            return True
        else:
            return False
            
                
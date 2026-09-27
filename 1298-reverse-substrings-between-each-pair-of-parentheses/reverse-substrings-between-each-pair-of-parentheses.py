class Solution:
    def reverseParentheses(self, s: str) -> str:
        st=[]
        for c in s:
            if(c==')'):
                temp=""
                while(st[-1]!='('):
                    temp+=st.pop()
                if(st):
                    st.pop()
                for ch in temp:
                    st.append(ch)
            else:
                st.append(c)
        ans=""
        while(st):
            ans+=st.pop()
        ans=''.join(reversed(ans))
        return ans


        
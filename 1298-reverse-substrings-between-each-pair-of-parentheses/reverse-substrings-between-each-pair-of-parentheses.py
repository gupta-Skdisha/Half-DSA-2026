class Solution:
    def reverseParentheses(self, s: str) -> str:
        ans=[""]
        for ch in s:
            if ch=="(":
                ans.append("")
            elif ch==")":
                t=ans.pop()
                ans[-1]+=t[::-1]
            else:
                ans[-1]+=ch
        return ans[0]
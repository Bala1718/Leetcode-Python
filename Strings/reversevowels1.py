class Solution:
    def reverseVowels(self, s: str) -> str:
        a=set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        i,j=0,len(s)-1
        s=list(s)
        while i<j:
            if s[i] not in a:
                i+=1
            elif s[j] not in a:
                j-=1
            if s[i] in a and s[j] in a:
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
        return "".join(s)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l=len(s)
        if l!=len(t):
            return False
        ds={}
        dt={}
        for i in range(l):
            ds[s[i]]=1+ds.get(s[i],0)
            dt[t[i]]=1+dt.get(t[i],0)
        return ds==dt
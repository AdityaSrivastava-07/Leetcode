class Solution:
    def frequencySort(self, s: str) -> str:
        l={}
        new=[]
        for i in s:
            if i in l:
                l[i]+=1
            else:
                l[i]=1
        num=list(l.values())
        st=list(l.keys())
        for i in range(len(st)):
            idx=num.index(max(num))
            new.append((num[idx])*st[idx])
            st.pop(idx)
            num.pop(idx)
        return "".join(new)
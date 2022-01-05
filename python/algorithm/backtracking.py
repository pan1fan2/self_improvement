res = []
n = 3
def backtrack(left,right,S):
    if len(S) == n*2:
        res.append(S)
        return
    else:
        if left < n:
            backtrack(left+1,right,S+'(')
        if left > right :
            backtrack(left,right+1,S+')')

backtrack(0,0,"")
print(res)
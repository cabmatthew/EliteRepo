class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if not s:
            return True
        idxS = 0
        idxT = 0
        while idxT < len(t) and idxS < len(s):
            if s[idxS] == t[idxT]:
                idxS += 1
                idxT += 1
            else:
                idxT += 1
        if idxS == len(s):
            return True
        return False
"""
abc ahbgdc
^   ^ 
abc ahbgdc
 ^   ^
abc ahbgdc
 ^    ^
abc ahbgdc
  ^    ^
abc ahbgdc
  ^     ^
abc ahbgdc
  ^      ^
abc ahbgdc
   ^      ^

axc ahbgdc
^   ^
axc ahbgdc
 ^   ^
axc ahbgdc
 ^    ^
axc ahbgdc
 ^     ^
axc ahbgdc
 ^      ^
axc ahbgdc
 ^       ^
axc ahbgdc
 ^        ^
if ptrS reaches end AND ptrT reaches end, return true
Edges (false):
- If len(s) > len(t) return false

have idxS and idxT
while idxT < len(t):
if s[idxS] == t[idxT]:
    idxS += 1, idxT += 1
else:
    idxT += 1


"""
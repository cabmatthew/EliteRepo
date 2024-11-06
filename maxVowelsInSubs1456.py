class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        count = 0 
        for i in range(k):
            if s[i].lower() in vowels:
                count += 1
        max = count
        ptrL = 0
        ptrR = k - 1
        while ptrR < len(s) - 1:
            if s[ptrL] in vowels:
                count -= 1
            if s[ptrR + 1] in vowels:
                count += 1

            if count > max:
                max = count
            ptrL += 1
            ptrR += 1

        return max
"""
count = 0
for i in range(k):
    if s[i] in vowels:
        count += 1
vowels = "aeiou"
ptrR = k - 1
ptrL = 0
while ptrR < len(s):  
    
    something something. s[L].lower()
"""
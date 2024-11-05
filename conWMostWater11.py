class Solution:
    def maxArea(self, height: List[int]) -> int:
        max = 0
        idxL = 0
        idxR = len(height) - 1
        while idxL != idxR:
            currentArea = min(height[idxL], height[idxR]) * (idxR - idxL)
            if currentArea > max:
                max = currentArea
            if height[idxL] < height[idxR]:
                idxL += 1
            else:
                idxR -= 1
        return max
"""
min(L,R) * (idxR - idxL)
start wide
move in the side w/ lower height
keep a max value

max = 0
while idxL != idxR:
    currentArea = min(height[L], height[R]) * (idxR - idxL)
    if currentArea > max:
        max = currentArea
"""
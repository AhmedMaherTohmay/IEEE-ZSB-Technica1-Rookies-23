class Solution(object):
    def lastStoneWeight(self, stones):
        l = count(stones)
        return l

def count(stones):
    while len(stones) > 1:
        m1 = max(stones)
        stones.remove(m1)
        m2 = max(stones)
        stones.remove(m2)
        stones.append(m1 - m2)
    if stones:
        return stones[0]
    else:
        return 0
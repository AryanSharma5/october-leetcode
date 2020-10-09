class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        ans = 0
        for b in count:
            if (k>0 and b-k in count) or (k==0 and count[b]>=2):
                ans += 1
        return ans
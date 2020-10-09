class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def findCombinationSum(candidates, target, idx, path):
            if target<0:
                return
            if target == 0:
                self.ans.append(path)
            for i in range(idx, len(candidates)):
                findCombinationSum(candidates, target - candidates[i], i, path + [candidates[i]])
                
        self.ans = []
        findCombinationSum(candidates, target, 0, [])
        return self.ans
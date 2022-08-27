class Solution(object):
    def combinationSum(self, cand, targ, start=0, solns=None, trace=None):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if solns is None:
            solns = []
            cand.sort()
        if trace is None:
            trace = []
        if targ == 0:
            solns.append(trace)
            return [trace]
        i = start
        while i < len(cand) and cand[i] <= targ:
            nt = targ - cand[i]
            self.combinationSum(cand, nt, i, solns, trace + [cand[i]])
            i += 1
        return solns


if __name__ == "__main__":
    candidates = list(map(int, input().split()))
    target = int(input())
    print(Solution().combinationSum(candidates, target))


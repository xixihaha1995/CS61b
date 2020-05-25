import collections


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent = list(range(len(s))
        def find(r):
            while parent[r] != r:
                parent[r] = find(parent[r])
            return r

        for l, r in pairs:
            pl = find(l)
            pr = find(r)
            if pl != pr:
                parent[pl] = pr

        mem = collections.defaultdict(list)
        for counter, value in enumerate(parent):
            mem[find(value)].append(s[counter])
        for sets in mem:
            mem[sets].sort(reverse = True)
        res = ""
        for i in range(len(s)):
            # mem can be itereated via original str index,
            # though mem have many different sets, all len(set) == len(original string)
            res.append(mem[find(i)].pop())
        return res





class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_map = defaultdict(set)
        for truster, trusted in trust:
            trust_map[truster].add(trusted)
        trusted_by_all = set.intersection(*[trusted_set for trusted_set in trust_map.values()])
        for person in trusted_by_all:
            if person not in trust_map:
                return person
        return -1
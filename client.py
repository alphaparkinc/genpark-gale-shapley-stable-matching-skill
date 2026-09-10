class GaleShapleyMatcher:
    """
    Gale-Shapley Deferred Acceptance Algorithm.
    Computes proposer-optimal stable matching in bipartite two-sided markets.
    """
    def __init__(self, proposers_pref, receivers_pref):
        self.proposers_pref = proposers_pref # proposer -> ranked list of receivers
        self.receivers_pref = receivers_pref # receiver -> ranked list of proposers

    def match(self):
        free_proposers = list(self.proposers_pref.keys())
        proposals_made = {p: 0 for p in free_proposers}
        matches = {} # receiver -> proposer

        while free_proposers:
            p = free_proposers[0]
            pref_list = self.proposers_pref[p]
            if proposals_made[p] >= len(pref_list):
                free_proposers.pop(0)
                continue

            r = pref_list[proposals_made[p]]
            proposals_made[p] += 1

            if r not in matches:
                matches[r] = p
                free_proposers.pop(0)
            else:
                current_p = matches[r]
                ranking = self.receivers_pref.get(r, [])
                if ranking.index(p) < ranking.index(current_p):
                    matches[r] = p
                    free_proposers.pop(0)
                    free_proposers.append(current_p)

        return {p: r for r, p in matches.items()}

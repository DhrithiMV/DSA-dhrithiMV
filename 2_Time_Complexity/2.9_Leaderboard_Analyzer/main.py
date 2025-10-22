# Leaderboard Analyzer
# Topic: Time & Space Complexity
# Type: Home Challenge

class Leaderboard:
    def __init__(self):
        self.scores = {}
    def addScore(self, playerId, score):
        if playerId not in self.scores:
            self.scores[playerId] = 0
        self.scores[playerId] += score
    def top(self, K):
        return sum(sorted(self.scores.values(), reverse=True)[:K])
    def reset(self, playerId):
        self.scores.pop(playerId, None)


# Demo
if __name__ == '__main__':
    sol = Solution()
    sol.leaderboard([50,70,90,60,80])
    sol.leaderboard([30,30,30])
    sol.leaderboard([100,40,60,80])


class HighScores:
    def __init__(self, scores):
        self.scores = scores
    
    def latest(self):
        return self.scores[-1]

    def list_of_scores(self):
        return self.scores

    def personal_top_three(self):
        return sorted(self.scores, reverse = True)[0:3]

    def personal_best(self):
        return sorted(self.scores, reverse = True)[0]

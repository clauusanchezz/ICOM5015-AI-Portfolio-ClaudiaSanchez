class PerformanceMeasure:

    def __init__(self):
        self.score = 0

    def update(self, environment, action):
        """
        Update cumulative performance.

        """
        self.score -= 1

        clean_squares = 0
        for location in environment.locations:
            if environment.dirt[location] == False:
                clean_squares += 1

        self.score += clean_squares

    def get_score(self):
        return self.score
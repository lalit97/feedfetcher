from django.db import models


class ScoreCard(models.Model):
    score = models.IntegerField()
    wicket = models.IntegerField()
    overs = models.IntegerField()

    def __str__(self):
        return f'{self.score}/{self.wicket} ({self.overs})'

from django.db import models


class BoastOrRoast(models.Model):
    TITLE_CHOICES = (
        ('b', 'boast'), ('r', 'roast'),
    )
    title = models.CharField(max_length=1, choices=TITLE_CHOICES)
    comment = models.CharField(max_length=280)
    upvote = models.PositiveIntegerField(default=0)
    downvote = models.PositiveIntegerField(default=0)

    @property
    def sum_votes(self):
        return self.upvote - self.downvote

    def __str__(self):
        return self.comment

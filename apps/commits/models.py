from django.db import models


class Commit(models.Model):
    score = models.IntegerField(default=0)
    score_funny = models.IntegerField(default=0)
    score_not_funny = models.IntegerField(default=0)
    text = models.TextField()
    git_hash = models.CharField(max_length=40, primary_key=True, unique=True)

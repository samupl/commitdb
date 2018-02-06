from django.db import models


class Commit(models.Model):
    score = models.IntegerField(default=0)
    score_funny = models.IntegerField(default=0)
    score_not_funny = models.IntegerField(default=0)
    text = models.TextField()
    git_hash = models.CharField(max_length=40, primary_key=True, unique=True)

    @classmethod
    def top_10(cls):
        return cls.objects.all().order_by('-score')[0:10]

    @classmethod
    def bottom_10(cls):
        return cls.objects.all().order_by('score')[0:10]

    @property
    def short_hash(self):
        return self.git_hash[:6]

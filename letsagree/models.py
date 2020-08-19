from django.db import models


class Term(models.Model):
    summary_en = models.CharField(max_length=40)

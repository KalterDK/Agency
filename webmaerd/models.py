from django.db import models


class Project(models.Model):
    image = models.ImageField(upload_to='portfolio/', help_text='Portfolio image')
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=200)
    url = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title


class Question(models.Model):
    title_short = models.CharField(max_length=200)
    title_long = models.CharField(max_length=200)
    text = models.TextField(max_length=1000)

    def __unicode__(self):
        return self.title_short

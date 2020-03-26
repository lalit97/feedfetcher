from django.db import models


class RssUrl(models.Model):
    url = models.CharField(max_length=100)

    def __str__(self):
        return str(self.url)


class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    link = models.CharField(max_length=200)

    def __str__(self):
        return str(self.title)

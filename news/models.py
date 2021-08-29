from django.db import models
from django.urls import reverse, resolve

# Model that contains keywords for searching such as AAPL, TWTR, etc
class Keyword(models.Model):
    title       = models.CharField(max_length = 120)

# Model with fetched news (keyword is a ForeignKey)
class New(models.Model):
    guid        = models.CharField(max_length = 100)
    title       = models.CharField(max_length = 200)
    pubDate     = models.DateTimeField(null = True)
    description = models.TextField(null = True)
    link        = models.CharField(max_length = 200)

    keyword = models.ForeignKey(Keyword, null = True, on_delete = models.SET_NULL)

    def get_absolute_url(self):
        return reverse("news:news-preview", kwargs = { "id" : self.id })

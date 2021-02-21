from django.db import models

# Create your models here.
  
class Favs(models.Model):
  reddit_post_id = models.TextField()
  title = models.TextField()
  author = models.TextField()
  body = models.TextField()
  created_utc = models.IntegerField()
  num_comments = models.IntegerField()
  image = models.TextField()
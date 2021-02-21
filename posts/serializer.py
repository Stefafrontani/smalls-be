from rest_framework import serializers
from .models import Favs

class FavSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Favs
    fields = [
      'id',
      'reddit_post_id',
      'title',
      'author',
      'body',
      'created_utc',
      'num_comments',
      'image',
    ]
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Favs
import json

from .serializer import FavSerializer

from django.views.decorators.csrf import csrf_exempt
 
@csrf_exempt
def index(request):
  if (request.method == 'GET'):
    fav_all = Favs.objects.all()
    favSerializer = FavSerializer(fav_all, many=True)
    return JsonResponse(favSerializer.data, safe=False)
  
  if (request.method == 'POST'):
    body_unicode = request.body.decode('utf-8')
    requestBody = json.loads(body_unicode)

    reddit_post_id = requestBody['reddit_post_id']
    title = requestBody['title']
    author = requestBody['author']
    body = requestBody['body']
    created_utc = requestBody['created_utc']
    num_comments = requestBody['num_comments']
    image = requestBody['image']

    fav = Favs(
      reddit_post_id=reddit_post_id,
      title=title,
      author=author,
      body=body,
      created_utc=created_utc,
      num_comments=num_comments,
      image=image,
    )
    fav.save()
    return HttpResponse(fav)

  if (request.method == 'DELETE'):
    post_id = request.body.decode('utf-8')
    post = Favs.objects.get(reddit_post_id=post_id)
    post.delete()
    return HttpResponse('Deleted succesfully')
  
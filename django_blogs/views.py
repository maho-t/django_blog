from django.shortcuts import render

from .models import Topic

def index(request):
  return render(request, 'django_blogs/index.html')

def topics(request):
  topics = Topic.objects.order_by('date_added')
  context = {'topics': topics}
  return render(request, 'django_blogs/topics.html', context)
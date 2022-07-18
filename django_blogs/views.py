from django import shortcuts
from django.shortcuts import render

def index(request):
  return render(request, 'django_blogs/index.html')
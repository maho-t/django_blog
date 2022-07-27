from html import entities
from multiprocessing import context
from django.shortcuts import redirect, render
from django.urls import is_valid_path
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

def index(request):
  return render(request, 'django_blogs/index.html')

@login_required
def topics(request):
  topics = Topic.objects.filter(owner=request.user).order_by('date_added')
  context = {'topics': topics}
  return render(request, 'django_blogs/topics.html', context)

@login_required
def topic(request, topic_id):
  topic = Topic.objects.get(id=topic_id)
  entries = topic.entry_set.order_by('-date_added')
  context = {'topic': topic, 'entries': entries}
  return render(request, 'django_blogs/topic.html', context)

@login_required
def new_topic(request):
  if request.method != 'POST':
    form = TopicForm()
  else:
    form = TopicForm(data=request.POST)
    if form.is_valid():
      form.save()
      return redirect('django_blogs:topics')

  context = {'form': form}
  return render(request, 'django_blogs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
  topic = Topic.objects.get(id=topic_id)
  if request.method != 'POST':
    form = EntryForm()
  else:
    form = EntryForm(data=request.POST)
    if form.is_valid():
      new_entry = form.save(commit=False)
      new_entry.topic = topic
      new_entry.save()
      return redirect('django_blogs:topic', topic_id=topic_id)

  context = {'topic': topic, 'form': form}
  return render(request, 'django_blogs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
  entry = Entry.objects.get(id=entry_id)
  topic = entry.topic

  if request.method != 'POST':
    form = EntryForm(instance=entry)
  else:
    form = EntryForm(instance=entry, data=request.POST)
    if form.is_valid():
      form.save()
      return redirect('django_blogs:topic', topic_id=topic.id)
  
  context = {'entry': entry, 'topic': topic, 'form': form}
  return render(request, 'django_blogs/edit_entry.html', context)
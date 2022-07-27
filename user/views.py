import imp
from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import is_valid_path

def register(request):
  if request.method != 'POST':
    form = UserCreationForm()
  else:
    form = UserCreationForm(data=request.POST)
    if form.is_valid():
      new_user = form.save()
      login(request, new_user)
      return redirect('django_blogs:index')
  
  context = {'form': form}
  return render(request, 'registration/register.html', context)
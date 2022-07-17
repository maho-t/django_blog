from pydoc_data.topics import topics
from tkinter import Toplevel
from django.contrib import admin

from .models import Topic

admin.site.register(Topic)
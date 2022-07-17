from pydoc_data.topics import topics
from tkinter import Toplevel
from django.contrib import admin

from .models import Entry, Topic

admin.site.register(Topic)
admin.site.register(Entry)
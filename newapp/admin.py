from django.contrib import admin
from .models import User, Group, ToDoList, NewFile

admin.site.register(User)
admin.site.register(Group)
admin.site.register(ToDoList)
admin.site.register(NewFile)
# Register your models here.

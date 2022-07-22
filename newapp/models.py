
from django.db import models
from django.contrib.auth.models import AbstractUser

class Group(models.Model):
    title = models.CharField(max_length=20)
    body = models.CharField(max_length=50, null=True)
    # icon = models.ImageField() # 이미지 필드는 기능 구현하고 추후에 해보는 걸로..

class User(AbstractUser):
    name = models.CharField(max_length = 200)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=13, null=True)
    gender = models.CharField(max_length=6, null=True)
    birthday = models.DateField(null=True)
    confirm = models.CharField(max_length=50, default='')

    # # 소속한 group의 이름들을 문자열 형식으로 받을 거임 (many to one 관계 표현하는 방법 모르겠음)
    # groups = models.CharField(max_length = 50, null=True) 

    # group =  models.ForeignKey(Group, null= True, on_delete = models.CASCADE) 
    # icon = models.ImageField() # 이미지 필드는 기능 구현하고 추후에 해보는 걸로..

class ToDoList(models.Model):
    title = models.CharField(max_length=20)
    body = models.CharField(max_length=50, null=True)
    enddate = models.DateField(null=True)
    writtendate = models.DateField(auto_now_add=True)
    is_first = models.IntegerField(null=True)
    is_end = models.IntegerField(null=True)
    # user = models.ForeignKey(User, null= True, on_delete = models.CASCADE)
    # group = models.ForeignKey(Group, null= True, on_delete = models.CASCADE) 

class NewFile(models.Model):
    myfile = models.FileField()


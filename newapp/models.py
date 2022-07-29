
from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     name = models.CharField(max_length = 200)
#     email = models.EmailField(null=True)
#     phone = models.CharField(max_length=13, null=True)
#     gender = models.CharField(max_length=6, null=True)
#     birthday = models.DateField(null=True)
#     confirm = models.CharField(max_length=50, default='')
 
#     # # 소속한 group의 이름들을 문자열 형식으로 받을 거임 (many to one 관계 표현하는 방법 모르겠음)
#     # groups = models.ForeignObject(many=True)

#     # group =  models.ForeignKey(Group, null= True, on_delete = models.CASCADE) 
#     # icon = models.ImageField() # 이미지 필드는 기능 구현하고 추후에 해보는 걸로..



class Group(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField(null=True)
    # thumbnail = models.ImageField(null=True)

    # users = models.ManyToManyField(User, null=True)
    # body = models.CharField(max_length=50, null=True)
    # icon = models.ImageField() # 이미지 필드는 기능 구현하고 추후에 해보는 걸로.

class ToDoList(models.Model):
    title = models.CharField(max_length=20)
    body = models.CharField(max_length=50, null=True)
    # enddate = models.DateField(null=True)
    writtendate = models.DateField(auto_now_add=True)
    is_first = models.IntegerField(default=0, null=True)
    is_end = models.IntegerField(default=0,null=True)
    # user = models.ForeignKey(User, null= True, on_delete = models.CASCADE)
    # group = models.ForeignKey(Group, null= True, on_delete = models.CASCADE) 

class NewFile(models.Model):
    # myfile = models.FileField()
    title = models.CharField(max_length=20, null=True)
    body = models.CharField(max_length=20, null=True)
    myfile = models.TextField()

class Notice(models.Model):
    # group = models.ForeignKey(Group, delete=models.CASCADE, default = 0, null=True)
    title = models.CharField(max_length=20)
    body = models.TextField()


from email.policy import default
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, name, password, phone, gender, birthday):
        user = self.model(
            email = email,
            name = name,
            phone = phone,
            gender = gender,
            birthday = birthday
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, name, password, phone, gender, birthday):
        user = self.create_user(
            email = email,
            name = name,
            password = password,
            phone = phone,
            gender = gender,
            birthday = birthday
        )
        user.is_admin = True
        user.save(using=self.db)
        return user



class User(AbstractBaseUser, PermissionsMixin):

    # email = models.EmailField(unique=True)
    # price = models.IntegerField(null=True)
    # sub_date = models.DateField(null=True)
    # nickname = models.CharField(max_length=100)
    # # subSet = models.ForeignKey(subSet, on_delete=models.CASCADE,null=True)
    # user_color = models.CharField(max_length=6, default="")
    name = models.CharField(max_length = 200)
    email = models.EmailField(unique=True, null=True)
    phone = models.CharField(max_length=13, null=True)
    gender = models.CharField(max_length=6, null=True)
    birthday = models.DateField(null=True)
    confirm = models.CharField(max_length=50, default='')

    # is_active = models.BooleanField(default=True)
    # is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def __str__(self):
        return self.email
    
    # def has_perm(self, perm, obj=None):
    #     return True
    
    # def has_module_perms(self, app_label):
    #     return True
    
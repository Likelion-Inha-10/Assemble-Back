
from dataclasses import field, fields
from rest_framework import serializers
from .models import User, ToDoList, NewFile, Group, Notice

class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    def create(self, validated_data):
        if validated_data['password'] == validated_data['confirm']:
            user = User.objects.create(username = validated_data['username'], name = validated_data['name'], 
            email = validated_data['email'], phone = validated_data['phone'], gender = validated_data['gender'], 
            birthday = validated_data['birthday'])
            user.set_password(validated_data['password'])
            user.save()
            return user
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'confirm', 'name', 'email', 'phone', 'gender', 'birthday']

# class ToDoListSerializer(serializers.ModelSerializer):
#     def get(self):
#         lists = ToDoList.objects.all()
#         return lists
#     class Meta:
#         model = ToDoList
#         fields = ['id', 'title']

# class LoginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username', 'password']

class ToDoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = '__all__'

class NewFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewFile
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    thumbnail = serializers.ImageField(use_url=True)
    class Meta:
        model = Group
        fields = '__all__'

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = '__all__'
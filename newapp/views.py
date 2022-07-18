from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, Group, ToDoList
from django.contrib import auth

# Create your views here.
class Test(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"meessage": "Hello, world!"})
    def post(self, request, *args, **kwargs):
        name = request.data['name']
        phone = request.data['phone']
        return Response({'name':name, 'phone':phone})

class First(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"test_message" : "Here is First page"})

class Signup(APIView):
    def post(selt, request, *args, **kwargs):

        username = request.data["username"]
        password = request.data["password"]
        password2 = request.data["confirm"]
        email = request.data["email"]
        phone = request.data["phone"]
        gender = request.data["gender"]
        birthday = request.data["birthday"]

        if password == password2:
            user = User.objects.create_user(username=username, password=password, email=email, phone=phone, gender=gender, birthday=birthday)
            auth.login(request, user)
            return Response({"message":"success", "username":username})
        else:
            return Response({"message":"fail"})

class Logout(APIView):
    def post(selt, request, *args, **kwargs):
        auth.logout(request)
        return Response({"message":"logout"})


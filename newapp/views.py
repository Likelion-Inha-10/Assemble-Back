from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from .serializers import SignupSerializer, ToDoListSerializer

# from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.authentication import authenticate
from .models import User, Group, ToDoList
# from newproject.newapp import serializers


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

class Signup(CreateAPIView):
    model = User()
    serializer_class = SignupSerializer 

class login(APIView):   #아직 구현 안 됨
    def post(self, request, *args, **kwargs):
        user = authenticate(username=request.data.get('username'),
                            password=request.data.get('password'))
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        else:
            return Response({"error": "invalid credentials"}, status=400)

class CreateToDoList(CreateAPIView):
    model = ToDoList()
    serializer_class = ToDoListSerializer

class FindToDoList(APIView):
    def get(self, request, tdl_id):
        tdl = get_object_or_404(ToDoList, pk = tdl_id)
        return Response({"message":"Details of To Do List", "id":tdl.id, "title":tdl.title, "body":tdl.body, "enddate":tdl.enddate, "writtendate":tdl.writtendate, "is_first":tdl.is_first, "is_end":tdl.is_end})

class Priority(APIView):
    def post(self, request, tdl_id):
        tdl = get_object_or_404(ToDoList, pk = tdl_id)
        if tdl.is_first == True:
            tdl.is_first = None
        else:
            tdl.is_first = True
        tdl.save()
        return Response({"message":"This is priority page", "title":tdl.title, "Priority":tdl.is_first})

class DeletedToDoList(APIView):
    def post(self,request, tdl_id):
        tdl = get_object_or_404(ToDoList, pk = tdl_id)
        tdl.delete()
        return Response({"message":"This list is deleted"})

class Main(APIView):
    def get(self, request):

        tdl = ToDoList.objects.filter().order_by('-is_first')
        serialized_rooms = ToDoListSerializer(tdl, many=True)
        return Response({"To Do Lists":serialized_rooms.data})
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from .serializers import GroupSerializer, NewFileSerializer, SignupSerializer, ToDoListSerializer
from rest_framework.parsers import FileUploadParser

# from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.authentication import authenticate
from .models import User, Group, ToDoList, NewFile


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

class FindToDoList(APIView):    # 수정 할 거임. Serializer 통해서 한번에 출력하기
    def get(self, request, tdl_id):
        tdl = get_object_or_404(ToDoList, pk = tdl_id)
        serialized_rooms = ToDoListSerializer(tdl)
        # return Response({"message":"Details of To Do List", "id":tdl.id, "title":tdl.title, "body":tdl.body, "enddate":tdl.enddate, "writtendate":tdl.writtendate, "is_first":tdl.is_first, "is_end":tdl.is_end})
        return Response({"ToDoList":serialized_rooms.data})

class Priority(APIView):
    def post(self, request, tdl_id):
        tdl = get_object_or_404(ToDoList, pk = tdl_id)
        if tdl.is_first == True:
            tdl.is_first = 0
        else:
            tdl.is_first = True
        tdl.save()
        return Response({"message":"This is priority page", "title":tdl.title, "is_first":tdl.is_first})
        
class EndList(APIView):
    def post(self, request, tdl_id):
        tdl = get_object_or_404(ToDoList, pk = tdl_id)
        if tdl.is_end == True:
            tdl.is_end = 0
        else:
            tdl.is_end = True
        tdl.save()
        return Response({"message":"This is end list page", "title":tdl.title, "is_end":tdl.is_end})

class DeletedToDoList(APIView):
    def post(self,request, tdl_id):
        tdl = get_object_or_404(ToDoList, pk = tdl_id)
        tdl.delete()
        return Response({"message":"This list is deleted"})

class Main(APIView):
    def get(self, request):

        tdl_1 = ToDoList.objects.filter(is_end=0).order_by('-is_first')
        tdl_2 = ToDoList.objects.filter(is_end=1)
        serialized_rooms_1 = ToDoListSerializer(tdl_1, many=True)
        serialized_rooms_2 = ToDoListSerializer(tdl_2, many=True)
        return Response({"To Do Lists":serialized_rooms_1.data, "End Lists":serialized_rooms_2.data})

class FileUploadView(APIView):
    parser_classes = (FileUploadParser,)

    def post(self, request):
        file = request.data.get('file', None)
        import pdb; pdb.set_trace()
        print(file)
        if file:
            newfile = NewFile()
            newfile.myfile = file
            newfile.save()
            return Response({"message": "File is received"}, status=200)
        else:
            return Response({"message": "File is missing"}, status=400)

class FileDownloadView(APIView):
    def get(self, request, file_id):
        file = get_object_or_404(NewFile, pk=file_id)
        serializers_room = NewFileSerializer(file)
        return Response({"File":serializers_room.data})

class CreateGroup(CreateAPIView):
    model = ToDoList()
    serializer_class = GroupSerializer
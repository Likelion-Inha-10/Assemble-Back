from http.client import ResponseNotReady
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from .serializers import GroupSerializer, NewFileSerializer, ToDoListSerializer, NoticeSerializer
from rest_framework.parsers import FileUploadParser

from django.contrib import auth
# from rest_framework.authtoken.models import Token
# from rest_framework.authentication import authenticate
from .models import User, Group, ToDoList, NewFile, Notice

from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator


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


# class login(APIView):   #아직 구현 안 됨
#     def post(self, request, *args, **kwargs):
#         user = authenticate(username=request.data.get('username'),
#                             password=request.data.get('password'))
#         if user is not None:
#             token, created = Token.objects.get_or_create(user=user)
#             return Response({"token": token.key})
#         else:
#             return Response({"error": "invalid credentials"}, status=400)

# @method_decorator(csrf_exempt,name='dispatch')
# @csrf_exempt
# class Login(APIView):
#     def post(self, request):
#         userid = request.data['username']
#         pwd = request.data['password']
#         user = auth.authenticate(request, username=userid, password=pwd)

#         if user is not None:
#             auth.login(request,user)
#             return Response({"message":"Login success"})
#         else:
#             return Response({"message":"Login Failed"})

class Login(APIView):
    def post(self, request, *args, **kwargs):
        userEmail = request.data["email"]
        pwd = request.data["password"]

        user = auth.authenticate(email=userEmail, password=pwd)

        # 유저 정보 확인
        if user is not None:
            auth.login(request, user)
            return Response({"id": user.id}, status=200)
        
        # 가입하지 않은 유저인 경우
        else:
            return Response({"message": "유저 정보가 없음"}, status=404)

class Logout(APIView):
    def post(self, request):
        auth.logout(request)
        return Response({"message":"Logout success"})

class Signup(APIView):
    def post(self, request, *args, **kwargs):

        # 이미 가입한 email인 경우
        if User.objects.filter(email=request.data['email']):
            return Response({"message": "이미 있는 email"}, status=409)
        
        # password1이랑 password2가 일치
        elif request.data["password1"] == request.data["password2"]:
            user = User.objects.create_user(
                email = request.data["email"],
                name = request.data["name"],
                password = request.data["password1"],
                phone = request.data["phone"],
                gender = request.data["gender"],
                birthday = request.data["birthday"]
            )
            #auth.login(request, user)   
            return Response({"message": "Success signup"}, status=201)

        # 불일치
        elif request.data["password1"] != request.data["password2"]:
            return Response({"message": "password가 일치하지 않음!!"}, status=400)


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
        group = Group.objects
        serialized_rooms_1 = ToDoListSerializer(tdl_1, many=True)
        serialized_rooms_2 = ToDoListSerializer(tdl_2, many=True)
        serialized_rooms_3 = GroupSerializer(group, many=True)
        return Response({"To Do Lists":serialized_rooms_1.data, "End Lists":serialized_rooms_2.data, "Groups":serialized_rooms_3.data})

# class FileUploadView(APIView):
#     # parser_classes = (FileUploadParser,)

#     # def post(self, request):
#     #     file = request.data.get('file', None)
#     #     import pdb; pdb.set_trace()
#     #     print(file)
#     #     if file:
#     #         newfile = NewFile()
#     #         newfile.myfile = file
#     #         newfile.save()
#     #         return Response({"message": "File is received"}, status=200)
#     #     else:
#     #         return Response({"message": "File is missing"}, status=400)

#     def post(self, request):
#         file = NewFile()
#         file.myfile = request.data['myfile']
#         file.save()
#         return Response({"message":"upload"})

class FileUploadView(CreateAPIView):
    model = NewFile()
    serializer_class = NewFileSerializer

class FileDownloadView(APIView):
    def get(self, request, file_id):
        file = get_object_or_404(NewFile, pk=file_id)
        serializers_room = NewFileSerializer(file)
        return Response({"File":serializers_room.data})

class DeleteFile(APIView):
    def post(self,request, file_id):
        file = get_object_or_404(ToDoList, pk = file_id)
        file.delete()
        return Response({"message":"This file is deleted"})

class CreateGroup(CreateAPIView):
    model = ToDoList()
    serializer_class = GroupSerializer

# class CreateGroup(APIView):
#     def post(self, request):
#         grp = Group()
#         grp.title = request.data['title']
#         grp.body = request.data['body']
#         grp.save()

        # if request.data['thumbnail'] == 'animal':
        #     # grp.thumbnail = Image(file='icon/animal.png', imgtype='png')
        #     # grp.thumbnail = 'https://user-images.githubusercontent.com/96401830/181812211-11f3386d-f107-4356-98c1-87710bec4556.png'
        #     img = open('https://user-images.githubusercontent.com/96401830/181812211-11f3386d-f107-4356-98c1-87710bec4556.png', 'r', encoding='utf-8')
        #     grp.thumbnail = img
        # elif request.data['thumbnail'] == 'company':
        #     grp.thumbnail = '/media/icon/company.png'
        # elif request.data['thumbnail'] == 'computer':
        #     grp.thumbnail = '/media/icon/computer.png'
        # elif request.data['thumbnail'] == 'food':
        #     grp.thumbnail = '/media/icon/food.png'
        # elif request.data['thumbnail'] == 'movie':
        #     grp.thumbnail = '/media/icon/movie.png'
        # elif request.data['thumbnail'] == 'music':
        #     grp.thumbnail = '/media/icon/music.png'
        # elif request.data['thumbnail'] == 'school':
        #     grp.thumbnail = '/media/icon/school.png'
        # elif request.data['thumbnail'] == 'study':
        #     grp.thumbnail = '/media/icon/study.png'
        # elif request.data['thumbnail'] == 'trip':
        #     grp.thumbnail = '/media/icon/trip.png'
        # elif request.data['thumbnail'] == 'workout':
        #     grp.thumbnail = '/media/icon/workout.png'
        # grp.save()
        # return Response({"title":grp.title, "body":grp.body})
        

class DeleteGroup(APIView):
    def post(self, request, grp_id):
        grp = get_object_or_404(Group, pk = grp_id)
        grp.delete()
        return Response({"message":"This group is deleted"})

class FileList(APIView):
    def get(self, request):
        files = NewFile.objects
        serialized_rooms = NewFileSerializer(files, many=True)

        return Response({"FileLists":serialized_rooms.data})

# 공지사항 부분, 안 하게 될 수도 있음 ======================

class CreateNotice(CreateAPIView):
    model = Notice()
    serializer_class = NoticeSerializer

class FindNotice(APIView):    
    def get(self, request, ntc_id):
        ntc = get_object_or_404(ToDoList, pk = ntc_id)
        serialized_rooms = ToDoListSerializer(ntc)
        return Response({"ToDoList":serialized_rooms.data})

class DeleteNotice(APIView):
    def post(self,request, ntc_id):
        ntc = get_object_or_404(ToDoList, pk = ntc_id)
        ntc.delete()
        return Response({"Notices":"This file is deleted"})

# ===================================================
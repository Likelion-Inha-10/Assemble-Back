from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class Test(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"meessage": "Hello, world!"})
    def post(self, request, *args, **kwargs):
        name = request.data['name']
        phone = request.data['phone']
        return Response({'name':name, 'phone':phone})
        
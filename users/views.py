from django.shortcuts import render
from rest_framework.response import Response
from .models import CustomUser
from .serializers import RegisterSerializer
from rest_framework.generics import GenericAPIView
from rest_framework import permissions,status
from rest_framework.decorators import api_view,permission_classes
# Create your views here.

class RegisterApi(GenericAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

    def post(self,request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Siz ruyxatdan utdingiz",'status':status.HTTP_201_CREATED})
        return Response({'error':serializer.errors,'status':status.HTTP_400_BAD_REQUEST})



@api_view(["GET"])
# @permission_classes([permissions.AllowAny])
def test(request):
    return Response({'data':True})

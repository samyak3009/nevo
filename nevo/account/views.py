from django.db import reset_queries
from rest_framework import response
from account.models import AccountUser
from account.serializers import AccountSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status

class AccountList(APIView):

    def get(self,request,format= None):
        print("hello")
        account = AccountUser.manager.all()
        serializer = AccountSerializer(account,many=True)
        return Response(serializer.data)

    def post(self,request,format= None):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class AccountDetail(APIView):

    def get_object(self,id):
        try:
            return AccountUser.manager.get(id=id)
        except AccountUser.DoesNotExist:
            return Http404

    def get(self,request,id,format=None):
        print("hello")
        account = self.get_object(id)
        serializer = AccountSerializer(account)
        return Response(serializer.data)
    
    def put(self, request, id, format=None):
        account = self.get_object(id)
        serializer = AccountSerializer(account, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id,format=None):
        account = self.get_object(id)
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

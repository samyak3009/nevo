from django.shortcuts import render
from django.core import serializers
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.views import APIView
from django.db.models import Q
from user.models import UserDetail
from user.serializers import UserSerializer
from rest_framework.decorators import api_view

def user_list(request):
    if request.method == 'POST':
        user_data = JSONParser().parse(request)
        print(user_data)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            print(user_serializer.data)
            return JsonResponse({'message': 'Data submitted successfully'}, status=status.HTTP_201_CREATED) 
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def user_detail(request):
    if request.method == 'GET':
        try: 
            id=request.GET.get('id')
            # user_data = UserDetail.objects.get(id=id)
            data = list(UserDetail.objects.filter(id=id).values('id','name','email','gender','user_name','date_of_birth'))
            # user = UserSerializer(user_data, many=False)
            if(len(data)>0):
                return JsonResponse({'data': data}, status=status.HTTP_201_CREATED)
            else:
                return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND)
        except UserDetail.DoesNotExist: 
            return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST':
        try:
            user_data = JSONParser().parse(request)
            data = list(UserDetail.objects.filter(Q(password=user_data['password']) & Q(user_name=user_data['username']) | Q(email=user_data['username'])).values('id','name','email','gender','user_name','date_of_birth'))
            if(len(data)>0):
                return JsonResponse({'data': data}, status=status.HTTP_201_CREATED)
            else:
                return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND)
        except UserDetail.DoesNotExist: 
            return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'PUT':
        try:
            id = request.GET.get('id')
            data = UserDetail.objects.get(id=id)
            user_data = JSONParser().parse(request)
            user_serializer = UserSerializer(data,data=user_data)
            if user_serializer.is_valid():
                user_serializer.save()
                print(user_serializer.data)
                return JsonResponse({'message': 'Data Updated successfully'}, status=status.HTTP_201_CREATED) 
            return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except UserDetail.DoesNotExist: 
            return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'DELETE':
        try:
            id = request.GET.get('id')
            data = UserDetail.objects.get(id=id)
            user_data = JSONParser().parse(request)
            data = UserDetail.objects.get(password=user_data['password'],id=id)
            data.delete() 
            return JsonResponse({'message': 'Account was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        except UserDetail.DoesNotExist: 
            return JsonResponse({'message': 'Wrong password'}, status=status.HTTP_404_NOT_FOUND)





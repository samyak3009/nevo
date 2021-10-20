from rest_framework import serializers 
from user.models import UserDetail

class UserSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = UserDetail
        fields = ('id',
                  'name',
                  'email',
                  'user_name',
                  'password',
                  'gender',
                  'date_of_birth')
 
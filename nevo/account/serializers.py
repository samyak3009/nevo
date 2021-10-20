from rest_framework import serializers 
from account.models import AccountUser

class AccountSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = AccountUser
        fields = ('id',
                  'email',
                  'name',
                  'username',
                  'active',
                  'staff',
                  'admin',
                  'password',
                  'gender',
                  'date_joined',
                  'last_login')
 
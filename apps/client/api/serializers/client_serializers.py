from rest_framework import serializers
from apps.client.models import User

class Create_ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = '__all__'
        
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class List_ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ('id','username', 'first_name','last_name','email','password')
        
        def to_representation(self, instance):
            return {
            'id':instance['id'],
            'username':instance['username'],
            'first_name':instance['first_name'],
            'last_name':instance['last_name'],
            'email':instance['email'],
            'password':instance['password']
            }
        
        
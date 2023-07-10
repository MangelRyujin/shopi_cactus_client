from rest_framework import serializers
from apps.client.models import User



class List_ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ('id','username', 'first_name','last_name','email')
        
        def to_representation(self, instance):
            return {
            'id':instance['id'],
            'username':instance['username'],
            'first_name':instance['first_name'],
            'last_name':instance['last_name'],
            'email':instance['email'],
            }
            
            
class ClientDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name','last_name','email','username')
        


class Create_ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = '__all__'
        
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

        
class UpdateClientSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ('username','email','first_name','last_name')

        
class Password_SetSerializer(serializers.Serializer):
    password = serializers.CharField(max_length =128,min_length =8, write_only = True)
    password2 = serializers.CharField(max_length =128,min_length =8, write_only = True)
    
    def validate(self,data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password':'Las contraseñas son incorrectas'})
        return data
    
    

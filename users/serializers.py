from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    email = serializers.EmailField(required=True)
    phone_number = serializers.CharField(max_length=30, required=False)
    password = serializers.CharField(write_only=True, min_length=8)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'password')
        
        
    def validate_password(self, value):
        """
           Password validation
        """  
        if len(value) < 8:
            raise serializers.ValidationError('Password must be at least 8 characters long.')
        return value
    
    def validate_email(self, value):
        """"
           Ensure email is not already taken.
        """
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('A user with email already exists.')
        return value
    
    def validate_phone_number(self, value):
        pass
    
    def create(self, validated_data):
        """
           Override the default create method to ensure the password is saved correctly.
        """
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password) # Hash the password
        user.save()
        return user  
        
class ResetPasswordSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, min_length=8)
    
    def validate_password(self, value):
        """
        Validate and return the password
        """ 
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long.")
        return value
    
    def update(self, instance, validated_data):
        """
        Custom update method to reset the password for the given user instance.
        """
        password = self.validate_password(validated_data['password'])
        instance.set_password(password) 
        instance.save()
        return instance       
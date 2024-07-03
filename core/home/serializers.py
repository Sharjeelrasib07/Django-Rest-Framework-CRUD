from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def validate(self, data):
        # Age validation
        if data.get('age', 0) < 18:
            raise serializers.ValidationError({'age_error': 'Age cannot be less than 18'})
        
        # Name validation
        if any(char.isdigit() for char in data.get('name', '')):
            raise serializers.ValidationError({'name_error': 'Name cannot contain numbers'})
        
        return data

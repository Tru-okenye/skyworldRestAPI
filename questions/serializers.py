from .models import Question,Response

from rest_framework import serializers

class QuestionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Question
        fields = '__all__'


class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = '__all__'
from rest_framework.serializers import Serializer
from rest_framework import serializers
from Corp.models import Corporations,Feedback
from Login.models import Compliants,Gann,Gscheme,Gjob

class PinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corporations
        fields = ['pincode']

class NameSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    

class DefaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corporations
        fields = ['name','address','pincode','latitude','longitude','phone_no']

class CompliantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compliants
        fields = ['email','name','address','contactnumber','compliants']
"""
{"email":"il",
"name":"d",
"address":"d",
"contactnumber":"dsfdd","compliants":"dsfgdgvdfvdf"}"""

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gann
        fields=['gannheading']

class SchemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gscheme
        fields=['gschemeheading']

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['email','name','msg']
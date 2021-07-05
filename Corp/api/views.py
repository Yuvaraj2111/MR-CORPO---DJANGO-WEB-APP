from django.http import request
from Login import api
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view,authentication_classes, permission_classes
from Login.views import Default
from django.contrib.auth import authenticate, login, logout
from Corp.api.serializers import PinSerializer, DefaultSerializer,NameSerializer,CompliantSerializer,AnnouncementSerializer,SchemeSerializer,FeedbackSerializer
from Corp.models import Corporations
from Login.models import Gann,Gjob,Gscheme
import json

@api_view(["POST"])
def pincode(request):
    scr=PinSerializer(data=request.data)
    if scr.is_valid():
        data1=Corporations.objects.filter(pincode= scr.data['pincode']).first()
        d =DefaultSerializer(data1)
        return Response(d.data)
    else:
        return Response(scr.errors)
"""
{
    "pincode":600023
}

"""
@api_view(["POST"])
def name(request):
    scr=NameSerializer(data=request.data)
    if scr.is_valid():
        data1=Corporations.objects.filter(name__iexact= scr.data['name']).first()
        d =DefaultSerializer(data1)
        return Response(d.data)
    else:
        return Response(scr.errors)

@api_view(["POST"])
def compliant(request):
    scr=CompliantSerializer(data=request.data)
    if scr.is_valid():
        scr.save()
        return Response({'valid':True})
    else:
        return Response(scr.errors)

@api_view(["GET"])
def ViewGovt(request):
    d1=Gann.objects.all()
    data1 = AnnouncementSerializer(d1,many=True)
    d2=Gscheme.objects.all()
    data2 = SchemeSerializer(d2,many=True)

    return Response({"anno":data1.data,"scheme":data2.data})

@api_view(["POST"])
def ViewFeedback(request):
    scr=FeedbackSerializer(data=request.data)
    if scr.is_valid():
        scr.save()
        return Response({'valid':True})
    else:
        return Response(scr.errors)


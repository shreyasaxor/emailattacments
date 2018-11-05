
# Create your views here.


# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
import requests
import os
from emailtest import settings
import zipfile
from django.core.mail import EmailMessage
from emailtest.settings import EMAIL_HOST_USER
from .utility import _sendemail,_zipfiles,_scrapfiles

class GetUser(APIView):

    def post(self,request,*args,**kwargs):
        FileNames=_scrapfiles(request.data['urls'])
        print "scraped"
        if _zipfiles(FileNames):
            pass
        print "zipped"
        if _sendemail(request.data['email']):
            print "mailed"
            return Response({'data':FileNames}, status=status.HTTP_200_OK)
        else:
            return Response({'data':'something went wrong'}, status=status.HTTP_200_OK)

get_user = GetUser.as_view()


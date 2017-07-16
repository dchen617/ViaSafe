from django.shortcuts import render
from django.http import HttpResponse
from django.template.defaulttags import csrf_token
from django.views.decorators.csrf import csrf_exempt
#from django.contrib.auth import Users
import requests
import logging
import json
import sys
from urllib.request import urlopen


def make():

    username = requests.POST.get('username')
    passW = requests.POST.get('pass')
    email = requests.POST.get('email')

    if(all(username, passW, email)):
        user = User(username=username, password=passW, email=email)

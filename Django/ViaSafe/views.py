from django.shortcuts import render
from django.http import HttpResponse
from django.template.defaulttags import csrf_token
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
import requests
import logging
import json
import sys
import os
import binascii
import re
from urllib.request import urlopen
from .models import Users  # TODO make use custom DJ one day


#@app.route("/test", methods=['POST', 'GET'])
@csrf_exempt
def locationParse(request):
    # https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=AIzaSyDs3AAMld7-LU0KNMsDZw5--624wOqpzOI&callback=initMap

    if request.method == 'POST':
        if(request.POST.get('area') is not None):
            # Get data from the front end as an address
            http = 'https://maps.googleapis.com/maps/api/geocode/json?address='
            key = '&key=AIzaSyDs3AAMld7-LU0KNMsDZw5--624wOqpzOI&callback=initMap'
            address = request.POST.get('address')  # TODO get value from frontend
            print(address)
            address = address.replace(' ', '+')
            ourReq = http + address + key

            respone = urlopen(ourReq)
            data = json.loads(respone.read().decode('utf8'))
            status = data['status']
            print(status)

            if(respone.getcode() == 200 and status == 'OK'):
                lng = data['results'][0]['geometry']['location']['lng']
                lat = data['results'][0]['geometry']['location']['lat']
                street = data['results'][0]['formatted_address']
                city = data['results'][0]['address_components'][2]['long_name']
                state = data['results'][0]['address_components'][5]['long_name']
                country = data['results'][0]['address_components'][6]['long_name']

                print(str(lng) + ' ' + str(lat) + ' ' + street + ' ' +
                      city + ' ' + state + ' ' + country)

            return render(request, 'index.html')

        # if we get it from the go location
        else:
            # https://maps.googleapis.com/maps/api/geocode/json?latlng=40.714224,-73.961452&key=AIzaSyDs3AAMld7-LU0KNMsDZw5--624wOqpzOI&callback=initMap
            http = 'https://maps.googleapis.com/maps/api/geocode/json?latlng='
            key = '&key=AIzaSyDs3AAMld7-LU0KNMsDZw5--624wOqpzOI&callback=initMap'
            lat = request.POST.get('lat')
            lng = request.POST.get('lng')
            ourReq = http + str(lat) + ',' + str(lng) + key

            respone = urlopen(ourReq)
            data = json.loads(respone.read().decode('utf8'))
            status = data['status']

            if(respone.getcode() == 200 and status == 'OK'):
                lng = data['results'][0]['geometry']['location']['lng']
                lat = data['results'][0]['geometry']['location']['lat']
                street = data['results'][0]['formatted_address']
                city = data['results'][0]['address_components'][2]['long_name']
                state = data['results'][0]['address_components'][5]['long_name']
                country = data['results'][0]['address_components'][6]['long_name']

                # print(respone.status_code, file=sys.stderr)
                print(str(lng) + ' ' + str(lat) + ' ' + street + ' ' +
                      city + ' ' + state + ' ' + country)
            else:
                return ('Please enter a vaild Address')
    else:
        return render(request, 'index.html')

    return render(request, 'index.html')


@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        passW = request.POST.get('pass')
        email = request.POST.get('email')
        token = binascii.b2a_hex(os.urandom(15))

        print(username + passW + email)

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return HttpResponse('Email is not vaild')

        if(all((username, passW, email))):
            if(Users.objects.filter(username=username).exists()):
                return HttpResponse('That username already exist, please enter another one]')
            elif(Users.objects.filter(email=email).exists()):
                return HttpResponse('The email already exist, plese enter another one')
            user = Users(username=username, passwordhash=passW, email=email, token=token)
            user.save()

    return HttpResponse('User has been created')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        try:
            user = Users.objects.get(username=username, passwordhash=password)
        except ():
            try:
                user = Users.objects.get(email=email, passwordhash=password)
            except Exception as e:
                return HttpResponse('Please give vaild login information')

        token = user.token
        return HttpResponse(token)

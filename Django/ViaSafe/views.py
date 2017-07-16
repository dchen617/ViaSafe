from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
import requests
import logging
import json
import sys


#@app.route("/test", methods=['POST', 'GET'])

def locationParse(request):
    # https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=AIzaSyDs3AAMld7-LU0KNMsDZw5--624wOqpzOI&callback=initMap

    var = False

    # if request.method == 'POST':

    # if we got it from the form do the below
    if(var):
        # Get data from the front end as an address
        http = 'https://maps.googleapis.com/maps/api/geocode/json?address='
        key = '&key=AIzaSyDs3AAMld7-LU0KNMsDZw5--624wOqpzOI&callback=initMap'
        address = '214 Ashton Glen, Durham NC'  # TODO get value from frontend
        address = address.replace(' ', '+')
        ourReq = http + address + key

        respone = requests.get(ourReq)
        data = respone.content
        data = json.loads(data)
        status = data['status']

        if(respone.status_code == 200 and status == 'OK'):
            lng = data['results'][0]['geometry']['location']['lng']
            lat = data['results'][0]['geometry']['location']['lat']
            street = data['results'][0]['formatted_address']
            city = data['results'][0]['address_components'][2]['long_name']
            state = data['results'][0]['address_components'][5]['long_name']
            country = data['results'][0]['address_components'][6]['long_name']

            print(str(lng) + ' ' + str(lat) + ' ' + street + ' ' +
                  city + ' ' + state + ' ' + country)
        else:
            return ('Please enter a vaild Address')

    # if we get it from the go location
    else:
        # https://maps.googleapis.com/maps/api/geocode/json?latlng=40.714224,-73.961452&key=AIzaSyDs3AAMld7-LU0KNMsDZw5--624wOqpzOI&callback=initMap
        http = 'https://maps.googleapis.com/maps/api/geocode/json?latlng='
        key = '&key=AIzaSyDs3AAMld7-LU0KNMsDZw5--624wOqpzOI&callback=initMap'
        lat = 35.9597944  # TODO get value from frontend
        lng = -78.8281028  # TODO get value from frontend
        ourReq = http + str(lat) + ',' + str(lng) + key

        respone = requests.get(ourReq)
        data = respone.content
        data = json.loads(data)
        status = data['status']

        if(respone.status_code == 200 and status == 'OK'):
            lng = data['results'][0]['geometry']['location']['lng']
            lat = data['results'][0]['geometry']['location']['lat']
            street = data['results'][0]['formatted_address']
            city = data['results'][0]['address_components'][2]['long_name']
            state = data['results'][0]['address_components'][5]['long_name']
            country = data['results'][0]['address_components'][6]['long_name']

            #print(respone.status_code, file=sys.stderr)
            print(str(lng) + ' ' + str(lat) + ' ' + street + ' ' +
                  city + ' ' + state + ' ' + country)
        else:
            return ('Please enter a vaild Address')

    return render(request,'index.html')

from django.shortcuts import render
from django.http import HttpResponse
from django.template.defaulttags import csrf_token
from django.views.decorators.csrf import csrf_exempt
from .models import *

# Create your views here.
import requests
import logging
import json
import sys
from urllib.request import urlopen


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
                # street = data['results'][0]['formatted_address']
                # city = data['results'][0]['address_components'][2]['long_name']
                # state = data['results'][0]['address_components'][5]['long_name']
                # country = data['results'][0]['address_components'][6]['long_name']

                # print(str(lng) + ' ' + str(lat) + ' ' + street + ' ' +
                      # city + ' ' + state + ' ' + country)
                return HttpResponse(json.dumps({'lng': lng, 'lat': lat}), content_type="application/json")

            # Return 400 if it couldn't parse the data
            context = {
                'status': '400', 'reason': 'could not find the address'  
            }
            response = HttpResponse(json.dumps(context), content_type='application/json')
            response.status_code = 400
            return response
            # return render(request, 'index.html')

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

                #print(respone.status_code, file=sys.stderr)
                print(str(lng) + ' ' + str(lat) + ' ' + street + ' ' +
                      city + ' ' + state + ' ' + country)
            else:
                return ('Please enter a vaild Address')
    else:
        return render(request, 'index.html')

    return render(request, 'index.html')

#send all locations to front end
@csrf_exempt
def getAll(request):
    # c = Locations.objects.all()
    # d2 = {"locations":c}
    x = 'USA'
    y = 'Texas'
    z = 'Dallas'

    country = Countries.objects.get(countryname = x)
    state = States.objects.get(statename = y, countryid = country.countryid)
    city = Cities.objects.get(cityname = z, stateid = state.stateid)
    location = Locations.objects.get(cityid = city.cityid, stateid = state.stateid, countryid = country.countryid)

    d = {"d": location}

    print(location.title)
    print(location.description)
    return render(request,'test.html', d)
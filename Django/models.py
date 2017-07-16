from __future__ import unicode_literals

from django.db import models


class Cities(models.Model):
    cityid = models.AutoField(primary_key=True)
    cityname = models.CharField(max_length=100)
    stateid = models.ForeignKey('States', db_column='stateid', on_delete=models.CASCADE)

    class Meta:
        db_table = 'cities'


class Countries(models.Model):
    countryid = models.AutoField(primary_key=True)
    countryname = models.CharField(max_length=100)

    class Meta:
        db_table = 'countries'


class Locations(models.Model):
    locationid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, blank=True, null=True)
    longitude = models.DecimalField(max_digits=12, decimal_places=8, blank=True, null=True)
    latitude = models.DecimalField(max_digits=12, decimal_places=8, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    countryid = models.ForeignKey(Countries, db_column='countryid', on_delete=models.CASCADE)
    stateid = models.ForeignKey('States', db_column='stateid', on_delete=models.CASCADE)
    cityid = models.ForeignKey(Cities, db_column='cityid', on_delete=models.CASCADE)
    userid = models.ForeignKey('Users', db_column='userid', on_delete=models.CASCADE)

    class Meta:
        db_table = 'locations'


class States(models.Model):
    stateid = models.AutoField(primary_key=True)
    statename = models.CharField(max_length=100)
    countryid = models.ForeignKey(Countries, db_column='countryid', on_delete=models.CASCADE)

    class Meta:
        db_table = 'states'


class Users(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, blank=True, null=True)
    passwordhash = models.CharField(max_length=1000, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    token = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        db_table = 'users'

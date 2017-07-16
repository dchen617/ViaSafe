# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cities(models.Model):
    cityid = models.AutoField(primary_key=True)
    cityname = models.CharField(max_length=100)
    stateid = models.ForeignKey('States', db_column='stateid', on_delete=models.CASCADE, on_update=models.CASCADE)

    class Meta:
        
        db_table = 'cities'


class Countries(models.Model):
    countryid = models.AutoField(primary_key=True)
    countryname = models.CharField(max_length=100)

    class Meta:
        
        db_table = 'countries'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        
        db_table = 'django_session'


class Locations(models.Model):
    locationid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, blank=True, null=True)
    longitude = models.DecimalField(max_digits=12, decimal_places=8, blank=True, null=True)
    latitude = models.DecimalField(max_digits=12, decimal_places=8, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    countryid = models.ForeignKey(Countries, db_column='countryid', on_delete=models.CASCADE, on_update=models.CASCADE)
    stateid = models.ForeignKey('States', db_column='stateid', on_delete=models.CASCADE, on_update=models.CASCADE)
    cityid = models.ForeignKey(Cities, db_column='cityid', on_delete=models.CASCADE, on_update=models.CASCADE)
    userid = models.ForeignKey('Users', db_column='userid', on_delete=models.CASCADE, on_update=models.CASCADE)

    class Meta:
        
        db_table = 'locations'


class States(models.Model):
    stateid = models.AutoField(primary_key=True)
    statename = models.CharField(max_length=100)
    countryid = models.ForeignKey(Countries, db_column='countryid', on_delete=models.CASCADE, on_update=models.CASCADE)

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
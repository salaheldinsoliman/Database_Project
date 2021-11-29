# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Capitals(models.Model):
    name = models.CharField(db_column='Name', primary_key=True, max_length=255)  # Field name made lowercase.
    population = models.CharField(db_column='Population', max_length=255)  # Field name made lowercase.
    area = models.CharField(db_column='Area', max_length=255)  # Field name made lowercase.
    governor = models.CharField(db_column='Governor', max_length=255)  # Field name made lowercase.
    coordinates = models.CharField(db_column='Coordinates', max_length=500)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'capitals'


class CountiresFinal(models.Model):
    name = models.CharField(db_column='Name', primary_key=True, max_length=255)  # Field name made lowercase.
    official_languages = models.CharField(db_column='Official_Languages', max_length=600, blank=True, null=True)  # Field name made lowercase.
    population = models.BigIntegerField(db_column='Population', blank=True, null=True)  # Field name made lowercase.
    density = models.FloatField(db_column='Density', blank=True, null=True)  # Field name made lowercase.
    driving_side = models.CharField(db_column='Driving_Side', max_length=255, blank=True, null=True)  # Field name made lowercase.
    calling_code = models.CharField(db_column='Calling_Code', max_length=255, blank=True, null=True)  # Field name made lowercase.
    time_zone = models.CharField(db_column='Time_Zone', max_length=255, blank=True, null=True)  # Field name made lowercase.
    continent = models.CharField(db_column='Continent', max_length=20, blank=True, null=True)  # Field name made lowercase.
    capital = models.CharField(db_column='Capital', max_length=255, blank=True, null=True)  # Field name made lowercase.
    area = models.FloatField(db_column='Area', blank=True, null=True)  # Field name made lowercase.
    waterpercentage = models.CharField(db_column='WAterPercentage', max_length=255, blank=True, null=True)  # Field name made lowercase.
    legislature = models.CharField(db_column='Legislature', max_length=600, blank=True, null=True)  # Field name made lowercase.
    ruler = models.CharField(db_column='Ruler', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hdi = models.CharField(db_column='HDI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    currency = models.CharField(db_column='Currency', max_length=255)  # Field name made lowercase.
    gdp_total = models.BigIntegerField(db_column='GDP_Total', blank=True, null=True)  # Field name made lowercase.
    gdp_capita = models.FloatField(db_column='GDP_Capita', blank=True, null=True)  # Field name made lowercase.
    gini = models.CharField(db_column='GINI', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'countires_final'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class RulersAll(models.Model):
    name = models.CharField(db_column='Name', primary_key=True, max_length=255)  # Field name made lowercase.
    birth_date = models.CharField(db_column='Birth_Date', max_length=255)  # Field name made lowercase.
    assumed_office = models.CharField(db_column='Assumed_Office', max_length=255)  # Field name made lowercase.
    political_party = models.CharField(db_column='Political_Party', max_length=255)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rulers_all'
        unique_together = (('name', 'country'),)


class Travels(models.Model):
    username = models.CharField(db_column='UserName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    traveldate = models.CharField(db_column='TravelDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rating = models.IntegerField(db_column='Rating', blank=True, null=True)  # Field name made lowercase.
    review = models.TextField(db_column='Review', blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'travels'


class Users(models.Model):
    email = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    birthdate = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'users'

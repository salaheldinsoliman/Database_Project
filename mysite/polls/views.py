from os import name
from django.shortcuts import render

from .models import CountiresFinal
from django.http import HttpResponse
from django.db import connection

import phonenumbers

def polls(request):
    cursor = connection.cursor()
    if request.method == "GET":
        phonenumber = request.GET.get('phone_number')
        print(phonenumber)
        x = phonenumbers.parse("+201124702202", None)
        if phonenumber is not None:
            x = phonenumbers.parse(phonenumber, None)
        calling_code= x.country_code
        stmt = "SELECT name FROM countires_final WHERE Calling_code='%s' "
        cursor.execute(stmt, [calling_code])
        for result in cursor:
            print(result)
        context = {"cursor":cursor}
    return render(request, "polls.html", context)



def polls2(request):
    cursor2 = connection.cursor()
    if request.method == "GET":
        GroupBy= request.GET.get('GroupBy')
        print (GroupBy)
        if GroupBy=='Area':
            stmt = "select name,area from countires_final order by Area desc limit 10"
        elif GroupBy=='GDP_Total':
            stmt = "select name,GDP_Total from countires_final order by GDP_Total desc limit 10"
        elif GroupBy=='GDP_Capita':
            stmt = "select name,GDP_Capita from countires_final order by GDP_Capita desc limit 10"
        elif GroupBy=='Population':
            stmt = "select name,Population from countires_final order by Population desc limit 10"
        elif GroupBy=='Density':
            stmt = "select name,Density from countires_final order by Density desc limit 10"
    cursor2.execute(stmt)
    for result in cursor2:
        print(result)
    
    context = {"cursor2":cursor2}
    return render(request, "polls.html", context)


def polls3(request):
    cursor3 = connection.cursor()
    stmt = "select name,Driving_side from countires_final WHERE Driving_side='left'"
    if request.method == "GET":
        DrivingDirection= request.GET.get('DrivingDirection')
        print(DrivingDirection)
        if DrivingDirection== 'left':
            stmt = "select name,Driving_side from countires_final WHERE Driving_side='left'"
        if DrivingDirection== 'right':
            stmt = "select name,Driving_side from countires_final WHERE Driving_side='right'"

    cursor3.execute(stmt)
    
  
    context = {"cursor3":cursor3}
    return render(request, "polls.html", context)


def polls4(request):
    cursor4 = connection.cursor()
    stmt = "BEGIN NULL END"
    if request.method == "GET":
        Country= [request.GET.get('Country')]
        print(Country)
        stmt="SELECT * FROM countires_final WHERE Name=%s"

    cursor4.execute(stmt,Country)
    context = {"cursor4":cursor4}
    return render(request, "polls.html", context)



def polls5(request):
    cursor5 = connection.cursor()
    stmt = "BEGIN NULL END"
    if request.method == "GET":
        Capital= [request.GET.get('Capital')]
        print(Capital)
        stmt="SELECT * FROM capitals WHERE Name=%s"

    cursor5.execute(stmt,Capital)
    context = {"cursor5":cursor5}
    return render(request, "polls.html", context)





def polls6(request):
    cursor6 = connection.cursor()
    stmt = "BEGIN NULL END"
    if request.method == "GET":
        Ruler= [request.GET.get('Ruler')]
        print(Ruler)
        stmt="SELECT * FROM rulers_all WHERE Name=%s"

    cursor6.execute(stmt,Ruler)
    context = {"cursor6":cursor6}
    return render(request, "polls.html", context)

def polls7(request):
    cursor7 = connection.cursor()
    stmt = "BEGIN NULL END"
    if request.method == "GET":
        Data= [request.GET.get('username'), request.GET.get('traveldate'), request.GET.get('rating'), request.GET.get('review'),request.GET.get('country')]
        print(Data)
        stmt ="INSERT INTO travels (username, traveldate, rating,review, country) VALUES (%s, %s, %s,%s , %s);"
    cursor7.execute(stmt,Data)
    context = {"cursor7":cursor7}
    return render(request, "polls.html", context)


def polls8(request):
    cursor8 = connection.cursor()
    stmt = "BEGIN NULL END"
    if request.method == "GET":
        Country_name= [request.GET.get('Country_name')]
        print(Country_name)
        stmt="SELECT * FROM travels WHERE country=%s"

    cursor8.execute(stmt,Country_name)
    context = {"cursor8":cursor8}
    return render(request, "polls.html", context)




def polls9(request):
    
    cursor9 = connection.cursor()
    stmt = "BEGIN NULL END"
    if request.method == "GET":
        Data= [request.GET.get('email'), request.GET.get('user_name'), request.GET.get('gender'), request.GET.get('age'),request.GET.get('birthdate')]
        print(Data)
        stmt ="INSERT INTO users (email, user_name, gender,age, birthdate) VALUES (%s, %s, %s,%s , %s);"
    cursor9.execute(stmt,Data)
    context = {"cursor9":cursor9}
    return render(request, "polls.html", context)
from django.urls import path

from . import views
from .views import polls,polls2

urlpatterns = [
    path('', views.polls, name='polls'),
    path('Func2/', views.polls2, name='polls2'),
    path('Func3/', views.polls3, name='polls3'),
    path('Func4/', views.polls4, name='polls4'),
    path('Func5/', views.polls5, name='polls5'),
    path('Func6/', views.polls6, name='polls6'),
    path('Func7/', views.polls7, name='polls7'),
    path('Func8/', views.polls8, name='polls8'),
    path('Func9/', views.polls9, name='polls9'),
]
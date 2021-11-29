from django.contrib import admin

# Register your models here.
from django.urls import include, path
from .models import CountiresFinal, Travels,Users,Capitals,RulersAll

admin.site.register(CountiresFinal)
admin.site.register(Users)
admin.site.register(Capitals)
admin.site.register(RulersAll)
admin.site.register(Travels)

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
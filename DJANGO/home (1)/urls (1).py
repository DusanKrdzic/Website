from django.urls import path
from . import views

urlpatterns = [
    
    path('en', views.english, name='english'),
    path('', views.deutsch, name='deutsch'),
    path('discoverBurgaltena', views.burgaltena, name='burgaltena'),
    path('en/discoverBurgaltena', views.burgaltenaEN, name='burgaltenaEN')
]

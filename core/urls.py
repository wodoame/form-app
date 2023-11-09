from django.urls import path 
import core.views as core_views
urlpatterns = [
    path('', core_views.index, name='index'),
    path('home/', core_views.home, name='home'),
    path('create-form/', core_views.createForm, name='create-form'),
]
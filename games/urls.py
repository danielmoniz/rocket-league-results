
from django.urls import path

from . import views

app_name = 'games'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.detail, name='details'),
    path('new', views.new, name='new'),
]

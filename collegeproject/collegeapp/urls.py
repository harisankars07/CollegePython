from django.urls import path
from .import views
app_name = 'collegeapp'

urlpatterns = [
    path('',views.home, name='home'),
    path('logins/', views.logins, name='logins'),
    path('register/', views.register, name='register'),
    path('new_page/', views.new_page, name='new_page'),
    path('form/', views.form, name='form'),
    path('confirm/', views.confirm, name='confirm'),
    path('get_courses/',views.get_courses, name='get_courses'),

]

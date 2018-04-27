from django.urls import path

from core import views

app_name = 'core'

urlpatterns = [
    path('login', views.SignInView.as_view(), name='login'),
    path('logout', views.logout_view, name='logout'),

    # nutritionist view
    path('nutritionist', views.nutritionist, name='nutritionist'),

]

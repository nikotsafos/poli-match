from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name="login"),
    path('signup', views.signup, name="signup"),
    path('politicians', views.politicians, name="politicians"),
    path('politician_detail', views.politician_detail, name="politician_detail"),
]
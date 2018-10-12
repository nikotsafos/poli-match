from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('signup', views.signup, name='signup'),
    path('politicians', views.politicians, name='politicians'),
    path('politicians/<int:pk>', views.politician_detail, name='politician_detail'),
    path('quotes/<int:pk>', views.quote_detail, name='quote_detail'),
    path('quotes', views.quotes, name='quotes'),
    path('politicians/new', views.politician_create, name='politician_create'),
    path('politicians/<int:pk>/edit', views.politician_edit, name='politician_edit'),
    path('politicians/<int:pk>/delete', views.politician_delete, name='politician_delete'),
    path('quotes/new', views.quote_create, name='quote_create'),
    path('quotes/<int:pk>/edit', views.quote_edit, name='quote_edit'),
    path('quotes/<int:pk>/delete', views.quote_delete, name='quote_delete'),
]
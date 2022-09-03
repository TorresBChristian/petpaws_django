from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('signout', views.signout, name='signout'),
    path('adopt', views.adopt, name='adopt'),
    path('give_up_for_adoption', views.give_up_for_adoption, name='give_up_for_adoption'),
]

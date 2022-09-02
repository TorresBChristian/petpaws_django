from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('adoptar', views.adoptar, name='adoptar'),
    path('dar_en_adopcion', views.give_up_for_adoption, name='dar_en_adopcion'),
    path('signout', views.signout, name='signout'),
]

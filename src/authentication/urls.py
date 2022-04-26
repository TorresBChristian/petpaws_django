from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('adoptar', views.adoptar, name='adoptar'),
    path('da_en_adopcion', views.da_en_adopcion, name='da_en_adopcion'),
]

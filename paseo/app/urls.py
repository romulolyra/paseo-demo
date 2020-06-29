from django.urls import path
from . import views
urlpatterns = [
    path('', views.log, name='login'),
    path('inicial/', views.inicial, name='inicial'),
    path('sobre-nos/', views.sobre, name='sobre'),
    path('cadastro/',views.cadastro, name='cadastro'),

]



from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('app.urls')),
    path('inicial/', include('app.urls')),
    path('cadastro/', include('app.urls')),
    path('admin/', admin.site.urls),


]
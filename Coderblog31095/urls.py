from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Appblog/', include('Appblog.urls')),
    path('userblog/', include('userblog.urls'))

]

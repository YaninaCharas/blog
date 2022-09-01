from django.urls import path
# from Appblog.views import experiencias,
from Appblog.views import inicio, provincias


urlpatterns = [
    path('experiencias/', provincias),
    path('', inicio)
]
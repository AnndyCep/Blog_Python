
from django.contrib import admin
from django.urls import path, include

from .Vistas import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', HomeView.as_view(), name = "home"),

    path('blog/', include('blog.urls', namespace='blog'))
]

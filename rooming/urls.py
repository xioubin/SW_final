
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    # path('', RedirectView.as_view(url='home/', permanent=True)),
]

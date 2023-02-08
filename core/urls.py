from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path("", TemplateView.as_view(template_name="index.html"),  name=""),
]

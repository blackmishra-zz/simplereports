from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('report/retail', views.report_ecommerce, name='retail_report'),
    path('report/marketing', views.report_marketing, name='retail_marketing'),
]

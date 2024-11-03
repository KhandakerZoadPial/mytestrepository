from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('authenticated_view', views.authenticated_view, name='authenticated_view')
]
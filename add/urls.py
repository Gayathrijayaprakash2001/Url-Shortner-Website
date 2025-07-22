from django.urls import path
from . import views
from .views import url_list_view
from .views import add_url
from . import views
urlpatterns = [
    path('', url_list_view, name='url_list'),
    path('', add_url, name='add_url'),
    path('add/', views.add_url, name='add_url'),
    path('edit/<int:pk>/', views.url_edit_view, name='url_edit'),
    path('delete/<int:pk>/', views.url_delete_view, name='url_delete'),




]

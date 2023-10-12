from django.urls import path
from . import views


urlpatterns = [
    path('page/', views.page_view, name='page_view'),
    path('secondary/', views.secondary_menu_view, name='secondary_meny'),
    path('third/', views.third_menu_view, name='third_meny')
]

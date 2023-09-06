from django.urls import path
from app.api import views

urlpatterns = [
    path('', views.WatchListAV.as_view(), name="watchlist"),
    path('<int:pk>/', views.WatchListDetailAV.as_view(), name="watchlist-detail"),

    path('platform/', views.StreamPlatformAV.as_view(), name='streamplatform-list'),
    path('platform/<int:pk>/', views.StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
]
from django.urls import path

from cv2web import views

urlpatterns = [
    path('', views.index, name="index"),
    path('cv2/', views.video_feed, name="video")
]
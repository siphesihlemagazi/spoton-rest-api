from django.urls import path

from api import views

urlpatterns = [
    path('materials/', views.MaterialAPIView.as_view()),
    path('material/detail/<str:id>/', views.MaterialDetails.as_view()),
]

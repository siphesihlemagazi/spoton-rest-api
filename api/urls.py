from django.urls import path

from api import views

urlpatterns = [
    path('material/', views.MaterialAPIView.as_view()),
    path('material/detail/<str:id>/', views.MaterialDetails.as_view()),
]

from django.urls import path

from api import views

urlpatterns = [
    path('materials/', views.MaterialList.as_view()),
    path('material/detail/<str:pk>/', views.MaterialDetail.as_view()),
]

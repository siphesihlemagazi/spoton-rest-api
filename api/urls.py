from django.urls import path
from api import views

urlpatterns = [
    path('materials/', views.material_list),
    path('material/detail/<str:pk>/', views.material_detail),
]

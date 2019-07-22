from django.urls import path
from . import views

urlpatterns = [
    path('', views.UpdateModelListAPIView.as_view()),
    path('<int:id>/', views.UpdateModelDetailAPIView.as_view()),
]
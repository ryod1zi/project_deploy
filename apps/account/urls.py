from django.urls import path
from . import views


urlpatterns = [
    path('', views.UserListView.as_view()),
    path('register/', views.RegistrationView.as_view())
]




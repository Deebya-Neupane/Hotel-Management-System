from django.urls import path
from .views import UserView, GroupView

urlpatterns = [
    path('register/',UserView.as_view({'post':'register'}),name='register'),
    path('login/',UserView.as_view({'post':'login'}),name='login'),
    path('role/',GroupView.as_view({'get':'list'}),name='role-listing'), 
]
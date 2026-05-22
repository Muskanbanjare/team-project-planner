from django.urls import path
from . import views

urlpatterns = [
  
    path('users/', views.user_api_view),
    path('teams/', views.team_api_view),
    path('teams/add-user/', views.add_user_to_team_view),
    path('boards/', views.board_api_view),
    path('tasks/', views.task_api_view),
    path('tasks/update/', views.task_update_view),
   

]


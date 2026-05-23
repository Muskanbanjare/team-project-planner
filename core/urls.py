from django.urls import path
from . import views

urlpatterns = [
  
    path('users/', views.user_api_view),
    path('users/<int:user_id>/',views.user_api_view),
    path('teams/', views.team_api_view),
    path('teams/<int:team_id>/',views.team_api_view),
    path('teams/add-user/',views.add_user_to_team_view),
    path('boards/', views.board_api_view),
    path('boards/<int:board_id>/', views.board_api_view),
    path('tasks/', views.task_api_view),
    path('tasks/<int:task_id>/', views.task_api_view),
    path('task-status/', views.task_status_view),
   

]


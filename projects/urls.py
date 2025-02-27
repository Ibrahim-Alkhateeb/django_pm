
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProjectListView.as_view(), name= 'project_list'),
    path('project/create/', views.ProjectCreateView.as_view(), name= 'project_create'),
    path('project/edit/<int:pk>', views.ProjectUpdateView.as_view(), name= 'project_update'),
    path('project/delete/<int:pk>', views.ProjectDeleteView.as_view(), name='project_delete'),
    path('task/create/', views.TaskCreateView.as_view(), name='task_create'),
    path('task/edit/<int:pk>/', views.TaskUpdateView.as_view(), name='task_update'),
    path('task/delete/<int:pk>', views.TaskDeleteView.as_view(), name='task_delete'),
]
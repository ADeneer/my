from django.urls import path
from . import views

urlpatterns = [
     path('', views.ShowProjectView.as_view(), name='home'),
     path('user/<str:username>', views.UserAllProjectView.as_view(), name='user-project'),
     path('project/<int:pk>', views.ProjectDetailView.as_view(), name='project-detail'),
     path('project/<int:pk>/update', views.UpdateProjectView.as_view(), name='project-update'),
     path('project/<int:pk>/delete', views.DeleteProjectView.as_view(), name='project-delete'),
     path('project/add', views.CreateProjectView.as_view(), name='project-add'),
     path('resume', views.resume, name='resume'),
]
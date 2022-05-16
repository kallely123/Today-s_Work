from . import views
from django.urls import path

urlpatterns = [

    path('',views.index,name='index'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbvhome/', views.TaskListview.as_view(), name='cbvhome'),
    path('cbvdetial/<int:pk>/', views.TaskDetialview.as_view(), name='cbvdetial'),
    path('cbvupdate/<int:pk>/', views.TaskUpdateview.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.TaskDeleteview.as_view(), name='cbvdelete'),
]

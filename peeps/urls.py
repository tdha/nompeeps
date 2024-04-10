from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    path('peeps/', views.peeps_index, name='index'),
    path('peeps/<int:peeps_id>/', views.peeps_detail, name='detail'),
    path('peeps/<int:peeps_id>/add_reminder/', views.add_reminder, name='add_reminder'),
    path('peeps/create', views.NompeepCreate.as_view(), name='peeps_create'),
    path('peeps/<int:pk>/update', views.NompeepUpdate.as_view(), name='peeps_update'),
    path('peeps/<int:pk>/delete', views.NompeepDelete.as_view(), name='peeps_delete'),

    path('groups/', views.GroupList.as_view(), name='groups_index'),
    path('groups/<int:pk>/', views.GroupDetail.as_view(), name='groups_detail'),
    path('groups/create/', views.GroupCreate.as_view(), name='groups_create'),
    path('groups/<int:pk>/update', views.GroupUpdate.as_view(), name='groups_update'),
    path('groups/<int:pk>/delete', views.GroupDelete.as_view(), name='groups_delete'),
]
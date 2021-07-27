from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("create/team", views.create_team, name='create_team'),
    path("team/<int:team_id>", views.detail, name='detail'),
    path("team/edit/<int:team_id>", views.edit, name="edit"),
    path("team/add/<int:team_id>", views.add_points, name="add"),
    path("team/delete/<int:team_id>", views.delete, name='delete'),
    path("rename/team/<int:team_id>", views.rename, name='rename'),
    path("create/member/<int:team_id>", views.create_member, name='create_member'),
    path("member/<int:team_id>/delete/<int:member_id>", views.delete_member, name='delete_member'),
    path("member/<int:member_id>/edit/<int:team_id>", views.edit_member, name="edit_member"),
]
from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

urlpatterns = [
    path('', views.notes_view),
    path('api/notes/<int:tag>/', views.notes_view),
    path('api/notes/', views.notes_view),
    path('api/notes/add/', views.add_note_view),
    path('api/notes/open/<note_id>/', views.open_note_view),
    path('api/notes/update', views.create_or_update_note_view),
    path('accounts/register/', views.register_view),
    path('accounts/login/', views.login_view),
    path('accounts/logout/', views.logout_view),
    path('accounts/edit/', views.account_edit_view)
]

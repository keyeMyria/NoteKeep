from django.urls import path

from notekeep.views import views
from notekeep.views.test_views import NotesTestView, TagsTestView

urlpatterns = [
    path('', views.notes_view),
    path('api/notes/<int:tag>/', views.notes_view),
    path('api/notes/', views.notes_view),
    path('api/notes/add/', views.add_note_view),
    path('api/notes/open/<note_id>/', views.open_note_view),
    path('api/notes/delete/<note_id>/', views.delete_note_view),
    path('api/notes/update', views.create_or_update_note_view),
    path('accounts/register/', views.register_view),
    path('accounts/login/', views.login_view),
    path('accounts/logout/', views.logout_view),
    path('accounts/edit/', views.account_edit_view),
    path('api/test/notes', NotesTestView.as_view()),
    path('api/test/tags', TagsTestView.as_view())
]

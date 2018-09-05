from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

urlpatterns = [
    path('', views.notes_view),
    path('api/notes/<int:tag>/', views.notes_view),
    path('api/notes/', views.notes_view),
    path('accounts/register/', views.register_view),
    path('accounts/login/', views.login_view),
    path('accounts/edit/', views.account_edit_view)

]

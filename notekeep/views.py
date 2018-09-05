from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

from notekeep.forms.RegisterForm import RegisterForm
from notekeep.models import Note
from notekeep.serializers import NotesSerializer


def register_view(request):
    """
    Registers an user or shows the form of registration. If the form is validated, the user is redirected to the
    login page
    :param request: the request containing all the information
    :return: a Validation exception or the redirection to the login page
    """
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(username=form.username, password=form.password, email=form.email)
            return HttpResponseRedirect('/accounts/login')
        else:
            return render(request, "registration/register.html", {"error": True})
    else:
        return render(request, "registration/register.html")


def login_view(request):
    """
    Tries to log in an user in to the database. After success, a redirect to the notes is called
    :param request: the request containing all the information
    :return: a Validation exception or the redirection to the login page
    """
    if request.method == 'POST':
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/api/notes')
        else:
            return render(request, "registration/login.html", {"error": True})
    else:
        return render(request, "registration/login.html")


@login_required
def notes_view(request, tag=0):
    notes_query = Note.objects.filter(user=request.user).order_by("created_at").all()
    notes = NotesSerializer(notes_query, many=True)
    return render(request, "notes.html", {"notes": notes.data})


@login_required
def account_edit_view(request):
    return render(request, "registration/account_edit.html")

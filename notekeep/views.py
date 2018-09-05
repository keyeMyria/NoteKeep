from time import sleep

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

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


def logout_view(request):
    """
    Log outs the current logged in user and redirects to login page
    :param request:
    :return:
    """
    logout(request)
    return HttpResponseRedirect('/accounts/login')


@login_required
def notes_view(request, tag=0):
    notes_query = Note.objects.filter(user=request.user).order_by("created_at").all()
    notes = NotesSerializer(notes_query, many=True)
    # sleep(5) # For test slow connections
    return render(request, "notes.html", {"notes": notes.data})


@login_required
def account_edit_view(request):
    return render(request, "registration/account_edit.html")


def add_note_view(request):
    """
    If the user is not authenticated, raises an error, else, shows an empty add note modal
    """

    print("Creating empty modal")

    if not request.user.is_authenticated:
        return HttpResponseBadRequest()
    else:
        return render(request, "notes/note_modal.html")


def open_note_view(request, note_id):
    """
    Gets the note with a given note id if exists and builds a modal then
    sends the modal to the frontend.
    If the user is not authenticated, raises an error
    """

    print("Building note modal for id: ", note_id)

    if request.user.is_authenticated:
        note = Note.objects.filter(user=request.user, id=note_id).first()
    else:
        return HttpResponseBadRequest()

    return render(request, "notes/note_modal.html", {"note": note})


@csrf_exempt
@api_view(['POST'])
def create_or_update_note_view(request):
    title = request.POST.get("title")
    body = request.POST.get("body")
    note_id = request.POST.get("id")

    if request.user.is_authenticated:
        Note.objects.update_or_create(id=note_id, defaults={"user": request.user, "title": title, "body": body})
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(data={"reason":"Unauthenticated user"}, status=status.HTTP_403_FORBIDDEN)
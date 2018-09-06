from rest_framework import generics

from notekeep.models import Note, Tag
from notekeep.serializers import NotesSerializer, TagsSerializer


class NotesTestView(generics.ListCreateAPIView):
    serializer_class = NotesSerializer

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)


class TagsTestView(generics.ListCreateAPIView):
    serializer_class = TagsSerializer

    def get_queryset(self):
        return Tag.objects.filter(user=self.request.user)
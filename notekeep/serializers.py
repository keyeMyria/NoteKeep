from rest_framework import serializers

from notekeep.models import Note


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = 'title', 'body'




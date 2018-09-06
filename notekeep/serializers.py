from rest_framework import serializers

from notekeep.models import Note, Tag


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class NotesSerializer(serializers.ModelSerializer):
    tags = TagsSerializer(read_only=True, many=True)

    class Meta:
        model = Note
        fields = 'title', 'body', 'tags', 'id'

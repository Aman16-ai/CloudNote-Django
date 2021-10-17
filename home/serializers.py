from django.db.models import fields
from rest_framework import serializers
from home.models import NotesInfo
class NotesSerializers(serializers.ModelSerializer):
    class Meta:
        model = NotesInfo
        fields = '__all__'
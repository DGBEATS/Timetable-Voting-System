from django.forms import ModelForm
from .models import Room


class RoomForm(ModelForm):
    class Meta: # create a form base on the meta data of the Room model
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants'] # exclude the host and participants meta data

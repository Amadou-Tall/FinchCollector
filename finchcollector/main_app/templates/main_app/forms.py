from django.forms import ModelForm
from .models import Habitat

class HabitatForm(ModelForm):
  class Meta:
    model = Habitat
    fields = '__all__'
    


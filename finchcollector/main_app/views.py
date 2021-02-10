from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch
from .forms import HabitatForm


class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'
    success_url = '/finches/'

class FinchUpdate(UpdateView):
    model = Finch
    fields = '__all__'

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/'    

def home(request):
  return render(request, 'home.html')
    
def about(request):
  return render(request, 'about.html')

def finches_index(request):
  finches = Finch.objects.all()
  return render(request, 'finches/index.html', {'finches': finches})

def finches_details(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  habitat_form = HabitatForm()
  habitats = finch.habitat_set.all()
  return render(request, 'finches/detail.html', { 'finch': finch, 'habitats': habitats })

def finch_Habitat(request, finch_id):
    form = HabitatForm(request.POST)
    if form.is_valid():
        new_habitat = form.save(commit=False)
        new_habitat.finch_id = finch_id
        new_habitat.save()
    return redirect('/finches/' + str(finch_id) + '/')

    

from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch



# finches = [
#     {'name': 'Frank', 'breed': 'House Finch', 'description': 'fast lil flyer', 'age': 2},
#     {'name': 'Mr. Tweets', 'breed': 'European Goldfinch', 'description': 'loves to talk', 'age': 5},
#     {'name': 'Prime Time', 'breed': 'American Goldfinch', 'description': 'loves attention but will bite', 'age': 10},
# ]
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {
        'finches': finches
    })

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)



    return render(request, 'finches/detail.html', { 
        'finch': finch 
    })

class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'
  
class FinchUpdate(UpdateView):
    model = Finch
    fields = ['breed', 'description', 'age']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches'

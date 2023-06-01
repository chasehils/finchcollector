from django.shortcuts import render
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


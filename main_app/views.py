import os
import uuid
import boto3
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Finch, Birdhouse, Photo
from .forms import FeedingForm

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
    id_list = finch.birdhouses.all().values_list('id')
    birdhouses_finch_doesnt_have = Birdhouse.objects.exclude(id__in=id_list)
    feeding_form = FeedingForm

    return render(request, 'finches/detail.html', { 
        'finch': finch, 'feeding_form': feeding_form,
        'birdhouses': birdhouses_finch_doesnt_have 
    })


class FinchCreate(CreateView):
    model = Finch
    fields = ['name', 'breed', 'description', 'age']
  
class FinchUpdate(UpdateView):
    model = Finch
    fields = ['breed', 'description', 'age']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches'


def add_feeding(request, finch_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect ('detail', finch_id=finch_id)

def assoc_birdhouse(request, finch_id, birdhouse_id):
    Finch.objects.get(id=finch_id).birdhouses.add(birdhouse_id)
    return redirect('detail', finch_id=finch_id)

def unassoc_birdhouse(request, finch_id, birdhouse_id):
    Finch.objects.get(id=finch_id).birdhouses.remove(birdhouse_id)
    return redirect('detail', finch_id=finch_id)

class BirdhouseList(ListView):
    model = Birdhouse

class BirdhouseDetail(DetailView):
    model = Birdhouse

class BirdhouseCreate(CreateView):
    model = Birdhouse
    fields = '__all__'

class BirdhouseUpdate(UpdateView):
    model = Birdhouse
    fields = ['name', 'color']

class BirdhouseDelete(DeleteView):
    model = Birdhouse 
    success_url = '/birdhouses'




def add_photo(request, finch_id):
  # photo-file maps to the "name" attr on the <input>
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    # Need a unique "key" (filename)
    # It needs to keep the same file extension
    # of the file that was uploaded (.png, .jpeg, etc.)
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      bucket = os.environ['S3_BUCKET']
      s3.upload_fileobj(photo_file, bucket, key)
      url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
      Photo.objects.create(url=url, finch_id=finch_id)
    except Exception as e:
      print('An error occurred uploading file to S3')
      print(e)
  return redirect('detail', finch_id=finch_id)

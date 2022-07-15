import imp
from django.shortcuts import redirect, render
from .models import Dog, Sport
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView,DetailView
from .forms import BidForm

# Create your views here.
# Define the home view
def home(request):
  return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def index(request):
    dogs=Dog.objects.all()
    return render(request,'dogs/index.html',{'dogs': dogs })

def detail(request,dog_id):
    dog= Dog.objects.get(id=dog_id)
    id_list = dog.sports.all().values_list('id')
    sports_dog_doesnt_have= Sport.objects.exclude(id__in=id_list)
    bid_form=BidForm()
    return render(request,'dogs/detail.html',{'dog':dog,'bid_form':bid_form,'sports': sports_dog_doesnt_have})

def assoc_sport(request, dog_id, sport_id):
  # Note that you can pass a sport's id instead of the whole sport object
  Dog.objects.get(id=dog_id).sports.add(sport_id)
  return redirect('detail', dog_id=dog_id)    

class DogCreate(CreateView):
    model=Dog
    fields='__all__'
    # success_url='/dogs/'

class DogUpdate(UpdateView):
    model=Dog
    fields=['breed','description','age']

class DogDelete(DeleteView):
    model=Dog
    success_url='/dogs/' 

def add_price(request,dog_id):
    form=BidForm(request.POST)
    if form.is_valid():
        new_price=form.save(commit=False)
        new_price.dog_id=dog_id
        new_price.save()
    return redirect('detail',dog_id=dog_id)   

class SportList(ListView):
    model=Sport     

class SportDetail(DetailView):
    model=Sport    

class SportCreate(CreateView):
    model=Sport
    fields='__all__'

class SportUpdate(UpdateView):
    model=Sport
    fields=['name']

class SportDelete(DeleteView):
    model=Sport
    success_url='/sports/' 


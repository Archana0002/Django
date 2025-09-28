from django.shortcuts import render
from . models import MovieInfo
# Create your views here.
from . forms import MovieForm
def create(request):
    frm = MovieForm()
    if request.POST:
        frm = MovieForm(request.POST)
        frm.is_valid
        title = request.POST.get('title')
        year = request.POST.get('year')
        desc = request.POST.get('description')
        movie_obj=MovieInfo(title=title,year=year,description=desc)
        movie_obj.save()

    return render(request,'create.html',{'frm':frm})

def list(request):
    movie_set=MovieInfo.objects.all()
    print(movie_set)
    return render(request,'list.html',{'movies':movie_set})

def edit(request):
    return render(request,'edit.html')

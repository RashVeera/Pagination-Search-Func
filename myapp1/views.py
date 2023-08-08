from django.shortcuts import render
from .models import Movie
from django.core.paginator import Paginator
# Create your views here.

def movieviewset(request):
    movie_object=Movie.objects.all()
    movie_name=request.GET.get('movie_name')
    if movie_name!='' and movie_name is not None:
        movie_object=movie_object.filter(name__icontains=movie_name)
    paginator=Paginator(movie_object,2)
    page=request.GET.get('page')
    movie_object=paginator.get_page(page)

    return render(request,'myapp1/movies.html',{'movie_object':movie_object})

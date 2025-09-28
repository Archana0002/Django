from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def print_hello(request):
    movie_data={'movies':[{ 'title':'godfather',
                     'year':2000,
                    'summary':'great',
                    'success':False
    },{'title':'anime',
                     'year':2000,
                    'summary':'great',
                    'success':True
    },{'title':'cartoon',
                     'year':2000,
                    'summary':'',
                    'success':False
    }]}
    return render(request,'hello.html',movie_data)

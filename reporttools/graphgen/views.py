from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from . import index_html

# Create your views here.
def index(request) :
#    body = index_html.index_view
 #   v
    template = loader.get_template("graphgen/index.html")
    return render(request,"graphgen/index.html")

def detail(request,det) :
    return HttpResponse(str(det))


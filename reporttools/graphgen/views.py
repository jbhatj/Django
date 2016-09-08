from django.shortcuts import render
from django.urls   import reverse
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from script import choose_qos_sm,fetch_details
from . import index_html
from fetch_data import do_connection
from chartit import DataPool,Chart
from .models import Machine,Machine_sjc1,Machine_dfw1,Machine_iad1
import time


# Create your views here.
def index(request) :
#    body = index_html.index_view
 #   v
    template = loader.get_template("graphgen/index.html")
    return render(request,"graphgen/index.html")

def detail(request) :
    product,analyzerId,from_time,to_time,cube_type = str(request.POST["product"]),str(request.POST["AnalyzerId"]),str(request.POST["from_time"]),str(request.POST["to_time"]),str(request.POST["CubeType"])
    pattern = "%Y-%m-%dT%H:%M"
    From_time = int(time.mktime(time.strptime(str(from_time),pattern)))
    To_time = int(time.mktime(time.strptime(str(to_time),pattern)))
    string = "product : %s <br> AnalyzerId : %s <br> Cube_type : %s <br> from Time : %s<br> To_Time : %s <br> "%(product,analyzerId,cube_type,from_time,to_time)
    do_connection(From_time,To_time,60,product,cube_type)


#    return HttpResponse(string)#string)#ou are corrently looking at this" + request.POST["product"])

#def dochart(request ) :
   # data = DataPool(series=[{ 'options' : { 'source' : Machine_sjc1.objects.all() }, 'terms' : ['bucket_time' , 'total_rules']}  ])
    data = DataPool(series=[{ 'options' : { 'source' : Machine_sjc1.objects.all() }, 'terms' : ['bucket_time' , 'total_rules']}, {'options' : { 'source' : Machine_iad1.objects.all() }, 'terms' : [{'bucket_time2' : 'bucket_time', 'total_rules2' : 'total_rules' }] }  ])
    chart = Chart(datasource=data,series_options=[{'options' : { 'type': 'line' , 'stacking' : True , 'color' : [ '#00cc00','#ff5050'] },'terms' : {'bucket_time' :['total_rules']}},{'options' : {'type' : 'line' ,'stacking' : True } , 'terms' : {'bucket_time2' : ['total_rules2']}}],chart_options = {'title': {'text': 'Time Vs TotaAl_Rules'}, 'xAxis': { 'title': {'text': 'Time'}}})
    #chart = Chart(datasource=data,series_options=[{'options' : { 'type': 'line' , 'stacking' : False},'terms' : {'bucket_time' :['total_rules']}}], [{'options' : {'type' : 'line', 'stacking' : False},'terms' : {'bucket_time' :['total_rules']}}],chart_options = {'title': {'text': 'Time Vs TotaAl_Rules'}, 'xAxis': { 'title': {'text': 'Time--->'}}})
   # return HttpResponse("do nothing")
    return  render(request,"graphgen/chart.html",{'chart' : chart })

def dochart(request ) :
    return HttpResponse("Do Nothing")

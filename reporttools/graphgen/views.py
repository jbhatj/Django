from django.shortcuts import render,render_to_response
from django.urls   import reverse
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from script import choose_qos_sm,fetch_details,generate_unique_id
from fetch_data import do_connection
from chartit import DataPool,Chart
from .models import Machine,Machine_sjc1,Machine_dfw1,Machine_iad1
import time


# Create your views here.
def index(request) :
#    Machine_sjc1.objects.all().delete()
#    Machine_dfw1.objects.all().delete()
#    Machine_iad1.objects.all().delete()
    return render(request,"graphgen/index.html")

def detail(request) :

    product,analyzerId,from_time,to_time,cube_type = str(request.POST["product"]),str(request.POST["AnalyzerId"]),str(request.POST["from_time"]),str(request.POST["to_time"]),str(request.POST.getlist("CubeType"))
#    if analyzerId == '' :
#        return render(request,"graphgen/index.html")
    pattern = "%Y-%m-%dT%H:%M"
    From_time = int(time.mktime(time.strptime(str(from_time),pattern)))
    To_time = int(time.mktime(time.strptime(str(to_time),pattern)))
    string = "product : %s <br> AnalyzerId : %s <br> Cube_type : %s <br> from Time : %s<br> To_Time : %s <br> "%(product,analyzerId,cube_type,from_time,to_time)
    uid = generate_unique_id()
    do_connection(From_time,To_time,60,product,cube_type,uid)
### Charting must be made as a different chart from above
    data = DataPool(series=[{ 'options' : { 'source' : Machine_sjc1.objects.filter(user_id = uid) }, 'terms' : [{'bucket_time1' : 'bucket_time', 'sjc1' : 'total_rules'}]},
                            { 'options' : { 'source' : Machine_iad1.objects.filter(user_id = uid) }, 'terms' : [{'bucket_time2' : 'bucket_time', 'iad1' : 'total_rules'}]},
                            { 'options' : { 'source' : Machine_dfw1.objects.filter(user_id = uid) }, 'terms' : [{'bucket_time3' : 'bucket_time', 'dfw1' : 'total_rules'}]}
                    ])
    chart =Chart(datasource=data,series_options=[ { 'options' : { 'type': 'line' , 'stacking' : False }, 'terms' : {'bucket_time1' : ['sjc1']}},
                                                  { 'options' : { 'type': 'line' , 'stacking' : False }, 'terms' : {'bucket_time2' : ['iad1']}},
                                                  { 'options' : { 'type': 'line' , 'stacking' : False } ,'terms' : {'bucket_time3' : ['dfw1']}}
                                                ],
                                 chart_options = {'title': {'text': 'Time Vs TotaAl_Rules'}, 'xAxis': { 'title': {'text': 'Time'}}, 'colors' : ['#4572A7', '#AA4643','#008080']})

    #return HttpResponse("do nothing")
    return  render(request,"graphgen/chart.html",{'chart' : chart })



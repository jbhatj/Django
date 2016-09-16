from django.conf.urls import url
from . import views

app_name="graphgen"

urlpatterns=[
    url(r'^$',views.index,name="index"),
    url(r'^detail$',views.detail,name="detail"),
#    url(r'^dochart$',views.dochart,name="dochart"),
    ]

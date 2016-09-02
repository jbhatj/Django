from django.conf.urls import url
from . import views

app_name="graphgen"

urlpatterns=[
    url(r'index',views.index,name="index"),
    #url(r'sourav/?P<details>[.*]$',views.detail,name="detail")
    url(r'sourav',views.detail,name="detail")
    ]

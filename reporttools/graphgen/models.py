from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Machine(models.Model) :
    machine_name = models.CharField(max_length=20)
    bucket_time = models.IntegerField(default=0)
    total_rules = models.IntegerField(default=0)
    def __str__(self) :
        return self.machine_name

class Machine_sjc1(models.Model) :
    user_id = models.CharField(max_length=1000)
    bucket_time = models.IntegerField(default=0)
    total_rules = models.IntegerField(default=0)
    def __str__(self) :
        return 'From sjc1'

class Machine_dfw1(models.Model) :
    user_id = models.CharField(max_length=1000)
    bucket_time = models.IntegerField(default=0)
    total_rules = models.IntegerField(default=0)
    def __str__(self) :
        return 'From dfw1'

class Machine_iad1(models.Model) :
    user_id = models.CharField(max_length=1000)
    bucket_time = models.IntegerField(default=0)
    total_rules = models.IntegerField(default=0)
    def __str__(self) :
        return 'From iad1'
     
class Users(models.Model) :
    AnalyzerId = models.IntegerField(default=0)
    AnalyzerName= models.CharField(max_length=1000)
    prod_type = models.CharField(max_length=10)

from django.db import models

class BaseClass(models.Model):
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now =True)
    
    class Meta:
        abstract =True

class CounterTable(BaseClass):
    last_staff_id = models.IntegerField(default=0)
    last_appoinment_id = models.IntegerField(default=0)
    last_payment_entry_id = models.IntegerField(default=0)

   
    


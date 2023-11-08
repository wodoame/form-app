from django.db import models

class VirtualForm(models.Model):
    title = models.CharField(max_length=128)
    form_fields = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.title  
    

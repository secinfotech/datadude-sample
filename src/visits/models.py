from django.db import models

# Create your models here.
class PageVisit(models.Model):
    #DB table and creates data as per model
    # id -> hidden -> primary key, autofield

    path = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
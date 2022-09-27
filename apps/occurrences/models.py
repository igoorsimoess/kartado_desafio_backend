from django.db import models

def upload_image(object, filename):
    return f'{object.created_at}-{filename}'

class Status(models.Model):
    name = models.CharField(max_length=50)
    color_hex = models.CharField(max_length=7)


class Road(models.Model):
    name = models.CharField(max_length=50)
    uf_code = models.CharField(max_length=2)
    length = models.FloatField()


class Occurrence(models.Model):

    @property
    def status_instance_name(self):
        return self.status.name
    
    @property
    def road_instance_name(self):
        return self.road.name

    description = models.CharField(max_length=50)
    road = models.ForeignKey(
        "occurrences.Road", null=True, on_delete=models.SET_NULL
    )
    road_name = road_instance_name
    km = models.CharField(max_length=50)    
    status = models.ForeignKey(
        "occurrences.Status", null=True, on_delete=models.SET_NULL
    )
    status_name = status_instance_name
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    occurrence_image = models.ImageField(upload_to=upload_image, blank=True, null=True) # models a field in order to receive the occurrence image 
    

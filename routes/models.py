from django.db import models

class Route(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_location = models.CharField(max_length=100)
    end_location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

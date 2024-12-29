from django.db import models

# Create your models here.
class PerfTitle(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

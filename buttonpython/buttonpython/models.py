from django.db import models
  
class Case(models.Case):
    case_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='media')
  
    def __str__(self):
        return self.case_name
from django.db import models
from django.urls import reverse

class Post(models.Model):
   title = models.CharField(max_length=20)
   body =models.TextField()

   class Meta:

      ordering =['id']

   def __str__(self):
      return str(self.id) + ' | '+ str(self.title)

   def get_absolute_url(self):
      return reverse('spinner_view')
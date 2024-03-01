from django.db import models
from django.utils.text import slugify

class section(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, null=True)
    
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(section, self).save(*args, **kwargs)

class dossier(models.Model):
    name = models.CharField(max_length=200)
    section_name = models.ForeignKey(section, on_delete=models.CASCADE, related_name="section_groupe")

    def __str__(self):
        return self.name
   




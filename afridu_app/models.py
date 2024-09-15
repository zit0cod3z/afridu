from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Registration(models.Model):
	name= models.CharField(max_length=200)
	nationality= models.CharField(max_length=200)
	dob = models.CharField(null=True, max_length=200)
	country= models.CharField(max_length=200)
	email= models.EmailField(null=True, max_length=200)
	attachment = models.ImageField(null=True, blank=True, upload_to="images")
	organization= models.CharField(max_length=200)
	position= models.CharField(blank=True, null=True, max_length=200)
	event= models.CharField(blank=True, null=True, max_length=2000)
	submitted_at= models.DateTimeField(auto_now_add=True)

	class Meta():
		ordering = ('-submitted_at',)

	def __str__(self):
		return f'Registration by {self.name} from {self.country} at {self.submitted_at} with image {self.attachment}'
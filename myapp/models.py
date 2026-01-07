from django.db import models
from ckeditor.fields import RichTextField
import uuid
# Create your models here.

class BannerModel(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title =RichTextField()
    description = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class TextModel(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    text =RichTextField()
    image = models.ImageField(upload_to='text/')
    sec_image = models.ImageField(upload_to='text/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class MainAbout(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    text = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class MeAbout(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = RichTextField()
    description = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class About(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    tagline =RichTextField()
    title = RichTextField()
    description = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class MinAbout(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title =RichTextField()
    description = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class MaxAbout(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title =RichTextField()
    description = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class EndAbout(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    thm_text =RichTextField()
    thm_btn = models.URLField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class SectionHeader(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    tagline =RichTextField()
    title = RichTextField()
    description = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

class Services(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    tagline =RichTextField()
    title = RichTextField()
    description = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

class ServiceOne(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = RichTextField()
    description = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

class ServiceTwo(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = RichTextField()
    description = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

class ServiceThree(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = RichTextField()
    description = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

class ServiceEnd(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    image = models.ImageField(upload_to='service_end/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
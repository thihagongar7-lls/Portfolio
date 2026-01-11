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

class Portfolio(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    tagline = RichTextField()
    title = RichTextField()
    description = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)     

class Card(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    pri_image = models.ImageField(upload_to='card/')
    sec_image = models.ImageField(upload_to='card/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

class Content(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = RichTextField()
    thm_pri_text = RichTextField()
    thm_sec_text = RichTextField()
    thm_btn= models.URLField(null=True,blank=True)
    thm_text = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   

class SecondCard(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    pri_image = models.ImageField(upload_to='sec_card/')
    sec_image = models.ImageField(upload_to='sec_card/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

class SecondContent(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = RichTextField()
    thm_pri_text = RichTextField()
    thm_sec_text = RichTextField()
    thm_third_text = RichTextField()
    thm_btn= models.URLField(null=True,blank=True)
    thm_text = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

class ThirdCard(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    pri_image = models.ImageField(upload_to='third_card/')
    sec_image = models.ImageField(upload_to='third_card/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

class ThirdContent(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = RichTextField()
    thm_pri_text = RichTextField()
    thm_sec_text = RichTextField()
    thm_third_text = RichTextField()
    thm_btn= models.URLField(null=True,blank=True)
    thm_text = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

class FourthCard(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    pri_image = models.ImageField(upload_to='fourth_card/')
    sec_image = models.ImageField(upload_to='fourth_card/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

class FourthContent(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = RichTextField()
    thm_pri_text = RichTextField()
    thm_sec_text = RichTextField()
    thm_btn= models.URLField(null=True,blank=True)
    thm_text = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    
class PortfolioEnd(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    thm_btn= models.URLField(null=True,blank=True)
    thm_text = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

class Experience(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    tagline = RichTextField()
    title = RichTextField()
    description = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)     

class Education(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = RichTextField()
    image = models.ImageField(upload_to='education/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   

class Trainer(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = RichTextField()
    min_title = RichTextField()
    description = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

class Assistant(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = RichTextField()
    min_title = RichTextField()
    description = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

class Design(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = RichTextField()
    min_title = RichTextField()
    description = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

class MinDesign(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = RichTextField()
    min_title = RichTextField()
    description = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

class Custom(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = RichTextField()
    image = models.ImageField(upload_to='custom/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

class MainContent(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    tagline = RichTextField()
    title = RichTextField()
    min_title = RichTextField()
    description = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

class MinContent(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    tagline = RichTextField()
    title = RichTextField()
    min_title = RichTextField()
    description = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

class ExperiencesImage(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    image = models.ImageField(upload_to='experiences_image/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)     

class HomePrice(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    tagline = RichTextField()
    title = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)     

class Starter(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = RichTextField()
    price = RichTextField()
    month = RichTextField()
    text = RichTextField()
    sec_text = RichTextField()
    third_text = RichTextField()
    thm_btn= models.URLField(null=True,blank=True)
    thm_text = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

class Basic(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = RichTextField()
    price = RichTextField()
    month = RichTextField()
    text = RichTextField()
    sec_text = RichTextField()
    third_text = RichTextField()
    fourth_text = RichTextField()
    five_text = RichTextField()    
    thm_btn= models.URLField(null=True,blank=True)
    thm_text = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Premium(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = RichTextField()
    price = RichTextField()
    month = RichTextField()
    text = RichTextField()
    sec_text = RichTextField()
    third_text = RichTextField()
    thm_btn= models.URLField(null=True,blank=True)
    thm_text = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class MainBlog(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    tagline = RichTextField()
    title = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   

class News(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    image = models.ImageField(upload_to='news/')
    user = RichTextField()
    time = RichTextField()
    title = RichTextField()
    thm_btn= models.URLField(null=True,blank=True)
    thm_text = RichTextField()    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  


class SecondNews(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    image = models.ImageField(upload_to='sec_news/')
    user = RichTextField()
    time = RichTextField()
    title = RichTextField()
    thm_btn= models.URLField(null=True,blank=True)
    thm_text = RichTextField()    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

class ThirdNews(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    image = models.ImageField(upload_to='third_news/')
    user = RichTextField()
    time = RichTextField()
    title = RichTextField()
    thm_btn= models.URLField(null=True,blank=True)
    thm_text = RichTextField()    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

class Touch(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = RichTextField()
    link = RichTextField()
    email = RichTextField()
    location = RichTextField()
    text = RichTextField()
    contact = RichTextField()
    phone = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Contact(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = RichTextField()
    submit = RichTextField() 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
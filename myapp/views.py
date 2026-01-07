from django.shortcuts import render
from .models import *

# Create your views here.

def Homepage(request):
    banner = BannerModel.objects.all()
    text = TextModel.objects.all()
    main_about = MinAbout.objects.all()
    me_about = MeAbout.objects.all()
    about =About.objects.all()
    min_about = MinAbout.objects.all()
    max_about =MaxAbout.objects.all()
    end_about =EndAbout.objects.all()
    section_header =SectionHeader.objects.all()
    services = Services.objects.all()
    service_one = ServiceOne.objects.all()
    service_two = ServiceTwo.objects.all()
    service_three =ServiceThree.objects.all()
    service_end = ServiceEnd.objects.all()
    contex = {
        'banner':banner,
        'text':text,
        'main_about':main_about,
        'me_about':me_about,
        'about':about,
        'min_about':min_about,
        'max_about':max_about,
        'end_about':end_about,
        'section_header':section_header,
        'services':services,
        'service_one':service_one,
        'service_two':service_two,
        'service_three':service_three,
        'service_end':service_end
    }
    return render(request, 'index.html', contex)
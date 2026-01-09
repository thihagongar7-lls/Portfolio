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

    portfolio = Portfolio.objects.all()
    card = Card.objects.all()
    content = Content.objects.all()
    second_card = SecondCard.objects.all()
    second_content = SecondContent.objects.all()
    third_card = ThirdCard.objects.all()
    third_content = ThirdContent.objects.all()
    fourth_card = FourthCard.objects.all()
    fourth_content = FourthContent.objects.all()
    portfolio_end = PortfolioEnd.objects.all()
    
    experience = Experience.objects.all()
    education =Education.objects.all()
    trainer = Trainer.objects.all()
    assistant =Assistant.objects.all()
    design = Design.objects.all()
    min_design = MinDesign.objects.all()
    custom = Custom.objects.all()
    main_content =MainContent.objects.all()
    min_content =MinContent.objects.all()
    experiences_image = ExperiencesImage.objects.all()
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
        'service_end':service_end,
        'portfolio': portfolio,
        'card':card,
        'content': content,
        'second_card':second_card,
        'second_content':second_content,
        'third_card':third_card,
        'third_content':third_content,
        'fourth_card':fourth_card,
        'fourth_content':fourth_content,
        'portfolio_end':portfolio_end,
        'experience':experience,
        'education':education,
        'trainer':trainer,
        'assistant':assistant,
        'design':design,
        'min_design':min_design,
        'custom':custom,
        'main_content':main_content,
        'min_content':min_content,
        'experiences_image':experiences_image
    }
    return render(request, 'index.html', contex)
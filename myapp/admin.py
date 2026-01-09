from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(BannerModel)
admin.site.register(TextModel)

admin.site.register(MainAbout)
admin.site.register(MeAbout)
admin.site.register(About)
admin.site.register(MinAbout)
admin.site.register(MaxAbout)
admin.site.register(EndAbout)

admin.site.register(SectionHeader)

admin.site.register(Services)
admin.site.register(ServiceOne)
admin.site.register(ServiceTwo)
admin.site.register(ServiceThree)
admin.site.register(ServiceEnd)

admin.site.register(Portfolio)
admin.site.register(Card)
admin.site.register(Content)
admin.site.register(SecondCard)
admin.site.register(SecondContent)
admin.site.register(ThirdCard)
admin.site.register(ThirdContent)
admin.site.register(FourthCard)
admin.site.register(FourthContent)
admin.site.register(PortfolioEnd)

admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Trainer)
admin.site.register(Assistant)
admin.site.register(Design)
admin.site.register(MinDesign)
admin.site.register(Custom)
admin.site.register(MainContent)
admin.site.register(MinContent)
admin.site.register(ExperiencesImage)

from landing import models
from django import template
from annoying.functions import get_object_or_None
register = template.Library()



@register.simple_tag(name='get_hero_section')
def get_hero_section():
    return get_object_or_None(models.HeroSection)


@register.simple_tag(name='get_about_us')
def get_about_us():
    return get_object_or_None(models.AboutUs)


@register.simple_tag(name='get_services')
def get_services():
    return models.Service.objects.order_by('?')[:3]


@register.simple_tag(name='get_download_apps')
def get_download_apps():
    return get_object_or_None(models.DownloadOurApps)


@register.simple_tag(name='get_partners')
def get_partners():
    return models.Partner.objects.all()
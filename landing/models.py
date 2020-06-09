
from django.db import models


class HeroSection(models.Model):
    title = models.CharField(max_length=150, verbose_name="Título")
    subtitle = models.CharField(max_length=500, null=True, blank=True, verbose_name="Subtítulo")
    image = models.ImageField(upload_to="web/images", verbose_name="Imágen")

    def __str__(self):
        return u"%s" % self.title

    class Meta:
        verbose_name = 'Sección Hero'
        verbose_name_plural = 'Sección Hero'


class AboutUs(models.Model):
    title = models.CharField(max_length=150, verbose_name="Título")
    description = models.CharField(max_length=500, null=True, blank=True, verbose_name="Descripción")

    def __str__(self):
        return u"%s" % self.title

    class Meta:
        verbose_name = 'Sobre Nosotros'
        verbose_name_plural = 'Sobre Nosotros'


class Service(models.Model):
    title = models.CharField(max_length=150, verbose_name="Título")
    description = models.CharField(max_length=500, null=True, blank=True, verbose_name="Descripción")
    icon = models.CharField(max_length=50, verbose_name="Icono", default="fa fa-check-square")

    def __str__(self):
        return u"%s" % self.title

    class Meta:
        verbose_name = 'Servicios'
        verbose_name_plural = 'Servicios'


class DownloadOurApps(models.Model):
    title = models.CharField(max_length=150, verbose_name="Título")
    description = models.CharField(max_length=500, null=True, blank=True, verbose_name="Descripción")
    image = models.ImageField(upload_to="web/images", verbose_name="Imágen")
    url_android = models.CharField(max_length=300, null=True, blank=True)
    url_ios = models.CharField(max_length=300, null=True, blank=True)
    url_windows = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return u"%s" % self.title

    class Meta:
        verbose_name = 'Descarga nuestras apps'
        verbose_name_plural = 'Descarga nuestras apps'


class Partner(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    logo = models.ImageField(upload_to="web/images")

    def __str__(self):
        return u"%s" % self.name

    class Meta:
        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'
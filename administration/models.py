from django.contrib.auth.models import User
from django.db import models
import datetime


class Company(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    cif = models.CharField(max_length=50, verbose_name="CIF")
    owner = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Dueño")
    photo = models.ImageField(upload_to="web/companies", default="web/companies/default_company.png", null=True, blank=True, verbose_name="Fotografía")
    employee_limit = models.IntegerField(default=0, verbose_name="Límite de trabajadores")

    def __str__(self):
        return u"%s" % self.name

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'



class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Usuario")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="Empresa")
    rol = models.IntegerField(default=0)

    def __str__(self):
        return u"%s" % self.user.username

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'


class Center(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    address = models.CharField(max_length=80, verbose_name="Dirección")
    workers = models.ManyToManyField(User, verbose_name="Trabajadores")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="Empresa")
    lat = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True, verbose_name="Latitud")
    lng = models.DecimalField(max_digits=11, decimal_places=8, null=True, blank=True, verbose_name="Longitud")

    def __unicode__(self):
        return self.name

    @property
    def total_time(self):
        journeys = self.workday_set.all()
        total = 0
        for j in journeys:
            total += j.total_time
        return total

    class Meta:
        verbose_name = 'Centro'
        verbose_name_plural = 'Centros'


class Project(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    workers = models.ManyToManyField(User, verbose_name="Trabajadores")
    estimated_time = models.TimeField(blank=True, null=True, verbose_name="Tiempo estimado")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Proyeto'
        verbose_name_plural = 'Proyectos'


class ProjectTime(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="Proyecto")
    date_start = models.DateTimeField(default=datetime.datetime.now, verbose_name="Fecha de inicio")
    date_end = models.DateTimeField(null=True, blank=True, verbose_name="Fecha de finalización")

    def __unicode__(self):
        return self.project.name

    class Meta:
        verbose_name = 'Tiempo de proyeto'
        verbose_name_plural = 'Tiempos de proyecto'

    @property
    def total_time(self):
        time = 0
        if self.date_end:
            time = self.date_end - self.date_start
        else:
            time = datetime.datetime.now() - self.date_start
        return time


class Workday(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    center = models.ForeignKey(Center, on_delete=models.CASCADE, verbose_name="Centro")
    comment_start = models.CharField(max_length=800, blank=True, null=True, verbose_name="Comentario de inicio")
    comment_end = models.CharField(max_length=800, blank=True, null=True, verbose_name="Comentario de finalización")
    date_start = models.DateTimeField(default=datetime.datetime.now, verbose_name="Fecha de inicio")
    date_end = models.DateTimeField(null=True, blank=True, verbose_name="Fecha de finalización")
    lat_start = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True, verbose_name="Latitud de inicio")
    lng_start = models.DecimalField(max_digits=11, decimal_places=8, null=True, blank=True, verbose_name="Longitud de inicio")
    lat_end = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True, verbose_name="Latitud de finalización")
    lng_end = models.DecimalField(max_digits=11, decimal_places=8, null=True, blank=True, verbose_name="Longitud de finalización")
    paused = models.BooleanField(default=False, verbose_name="Pausada")

    class Meta:
        ordering = ['user']
        verbose_name = 'Jornada'
        verbose_name_plural = 'Jornadas'

    def __unicode__(self):
        return self.user.username

    @property
    def get_pauses(self):
        return self.pause_set.all()

    @property
    def name(self):
        return self.user.first_name

    @property
    def total_time(self):
        time = 0
        if self.date_end:
            time = self.date_end - self.date_start
        else:
            print (datetime.datetime.now())
            print(self.date_start)
            # time = datetime.datetime.now(datetime.timezone.utc) - self.date_start

        pauses = self.get_pauses
        for pause in pauses:
            if pause.date_end:
                result = pause.date_end - pause.date_start
            else:
                result = datetime.datetime.now() - pause.date_start
            time = time - result

        time = ':'.join(str(time).split(':')[:2])
        return time


class Pause(models.Model):
    workday = models.ForeignKey(Workday, on_delete=models.CASCADE, verbose_name="Jornada")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="Proyecto", null=True, blank=True)
    comment_start = models.CharField(max_length=50, default="ND", verbose_name="Comentario de inicio")
    comment_end = models.CharField(max_length=50, default="ND", verbose_name="Comentario de finalización")
    date_start = models.DateTimeField(default=datetime.datetime.now, verbose_name="Fecha de inicio")
    date_end = models.DateTimeField(null=True, blank=True, verbose_name="Fecha de finalización")
    lat_start = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True, verbose_name="Latitud de inicio")
    lng_start = models.DecimalField(max_digits=11, decimal_places=8, null=True, blank=True, verbose_name="Longitud de inicio")
    lat_end = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True, verbose_name="Latitud de finalización")
    lng_end = models.DecimalField(max_digits=11, decimal_places=8, null=True, blank=True, verbose_name="Longitud de finalización")

    def __unicode__(self):
        return self.workday.user.username

    @property
    def user(self):
        return self.workday.user

    @property
    def center(self):
        return self.workday.center

    class Meta:
        verbose_name = 'Pausa'
        verbose_name_plural = 'Pausas'
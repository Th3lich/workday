from django.contrib.auth.models import User
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    cif = models.CharField(max_length=50, verbose_name="CIF")
    owner = models.ForeignKey(User, verbose_name="Dueño")
    photo = models.ImageField(upload_to="web/images", null=True, blank=True, verbose_name="Fotografía")
    employee_limit = models.IntegerField(default=0, verbose_name="Límite de trabajadores")

    def __str__(self):
        return u"%s" % self.name

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'



class Employee(models.Model):
    user = models.ForeignKey(User, verbose_name="Usuario")
    company = models.ForeignKey(Company, verbose_name="Empresa")
    rol = models.IntegerField(default=0)

    def __str__(self):
        return u"%s" % self.user.username

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
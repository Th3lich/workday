from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.template.defaultfilters import slugify


class Provincia(models.Model):
    nombre = models.CharField(max_length=25)
    nombre_slug = models.SlugField(blank=True, editable=False)

    def __str__(self):
        return u"%s" % self.nombre_slug

    def save(self, *args, **kwargs):
        self.nombre_slug = slugify(self.nombre)
        super(Provincia, self).save(*args, **kwargs)

    def toJSON(self):
        json = {'pk': self.pk,
                'nombre': self.nombre,
                'ciudad': self.nombre}
        return json


class Ciudad(models.Model):
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    nombre_slug = models.SlugField(blank=True, editable=False)

    def __str__(self):
        return u"%s" % self.provincia.nombre + " - " + u"%s" % self.nombre

    def save(self, *args, **kwargs):
        self.nombre_slug = slugify(self.nombre)
        super(Ciudad, self).save(*args, **kwargs)

    def toJSON(self):
        json = {'pk': self.pk,
                'nombre': self.provincia.nombre,
                'ciudad': self.nombre}
        return json


class TipoDieta(models.Model):
    nombre = models.CharField(max_length=300)
    nombre_slug = models.SlugField(blank=True, editable=False)

    def __str__(self):
        return u"%s" % self.nombre_slug


    def save(self, *args, **kwargs):
        self.nombre_slug = slugify(self.nombre)
        super(TipoDieta, self).save(*args, **kwargs)


class TipoCocina(models.Model):
    nombre = models.CharField(max_length=300)
    nombre_slug = models.SlugField(blank=True, editable=False)

    def __str__(self):
        return u"%s" % self.nombre_slug


    def save(self, *args, **kwargs):
        self.nombre_slug = slugify(self.nombre)
        super(TipoCocina, self).save(*args, **kwargs)


class Restaurante(models.Model):
    tipo_dieta = models.ForeignKey(TipoDieta, on_delete=models.CASCADE)
    tipo_cocina = models.ManyToManyField(TipoCocina, verbose_name="Tipos de cocina")
    nombre = models.CharField(max_length=300)
    nombre_fiscal = models.CharField(max_length=60, null=True, blank=True)
    nombre_slug = models.SlugField(blank=True, editable=False)
    ubicacion_x = models.CharField(max_length=100)
    ubicacion_y = models.CharField(max_length=100)
    direccion = models.CharField(max_length=500)
    direccion_fiscal = models.CharField(max_length=100, null=True, blank=True)
    CIF = models.CharField(max_length=15)
    codigo_postal = models.CharField(max_length=5)
    codigo_postal_fiscal = models.CharField(max_length=5, null=True, blank=True)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    provincia_fiscal = models.CharField(max_length=25, null=True, blank=True)
    localidad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    localidad_fiscal = models.CharField(max_length=25, null=True, blank=True)
    foto_perfil = models.ImageField(upload_to='imagenes/restaurante/', blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    publicar = models.BooleanField(default=True)
    descripcion = models.TextField()
    codigoqr = models.CharField(max_length=500)
    face = models.CharField(max_length=500, blank=True, null=True)
    insta = models.CharField(max_length=500, blank=True, null=True)
    twi = models.CharField(max_length=500, blank=True, null=True)
    web = models.CharField(max_length=500, blank=True, null=True)
    dog = models.BooleanField(default=False)
    domicilio = models.BooleanField(default=False)
    recoger = models.BooleanField(default=False)
    sin_gluten = models.BooleanField(default=False)
    destacado = models.BooleanField(default=False)
    valoracion_total = models.FloatField(default=1)
    coste_resparto_cliente = models.FloatField(default=0)

    def __str__(self):
        return u"%s" % self.nombre_slug


    def save(self, *args, **kwargs):
        self.nombre_slug = slugify(self.nombre)
        super(Restaurante, self).save(*args, **kwargs)


class Tienda(models.Model):
    nombre = models.CharField(max_length=300)
    nombre_fiscal = models.CharField(max_length=60, null=True, blank=True)
    nombre_slug = models.SlugField(blank=True, editable=False)
    ubicacion_x = models.CharField(max_length=100, blank=True, null=True)
    ubicacion_y = models.CharField(max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=500)
    direccion_fiscal = models.CharField(max_length=100, null=True, blank=True)
    CIF = models.CharField(max_length=15)
    codigo_postal = models.CharField(max_length=5, blank=True, null=True)
    codigo_postal_fiscal = models.CharField(max_length=5, null=True, blank=True)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, blank=True,null=True)
    provincia_fiscal = models.CharField(max_length=25, null=True, blank=True)
    localidad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, blank=True, null=True)
    localidad_fiscal = models.CharField(max_length=25, null=True, blank=True)
    foto_perfil = models.ImageField(upload_to='imagenes/restaurante/', blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    publicar = models.BooleanField(default=True)
    descripcion = models.TextField()
    codigoqr = models.CharField(max_length=500)
    face = models.CharField(max_length=500, blank=True, null=True)
    insta = models.CharField(max_length=500, blank=True, null=True)
    twi = models.CharField(max_length=500, blank=True, null=True)
    web = models.CharField(max_length=500, blank=True, null=True)
    solo_fisica = models.BooleanField(default=False)
    solo_online = models.BooleanField(default=False)
    destacada = models.BooleanField(default=False)


    def __str__(self):
        return u"%s" % self.nombre_slug


    def save(self, *args, **kwargs):
        self.nombre_slug = slugify(self.nombre)
        super(Tienda, self).save(*args, **kwargs)


class Galeria(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, null=True,blank=True)
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE , null=True,blank=True)
    nombre = models.CharField(max_length=300, blank=True, null=True)
    nombre_slug = models.SlugField(blank=True, editable=False)
    imagen = models.ImageField(upload_to='imagenes/restaurante/galeria')
    fecha = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        self.nombre_slug = slugify(self.nombre)
        super(Galeria, self).save(*args, **kwargs)

    def __str__(self):
        return u"%s_%s" % (self.restaurante, self.nombre)


class Valoracion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, null=True,blank=True)
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE , null=True,blank=True)
    calidad = models.IntegerField()
    espera = models.IntegerField()
    comida = models.IntegerField()
    valoracion_media = models.FloatField(default=1)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return u"%s_%s_%s_%s" % (self.restaurante.nombre, self.usuario.username, self.valoracion_media, self.fecha)


    def save(self, *args, **kwargs):


        valoracion_media = (self.calidad + self.espera + self.comida) / 3

        self.valoracion_media = valoracion_media

        valoraciones = Valoracion.objects.filter(restaurante=self.restaurante)

        valoracion_final = valoracion_media
        for v in valoraciones:
            print(valoracion_final)
            valoracion_final += v.valoracion_media
            print(valoracion_final)
            print(v.restaurante.nombre_slug)

        valoracion_final = valoracion_final / (valoraciones.count()+1)


        self.restaurante.valoracion_total = valoracion_final
        self.restaurante.save()


        super(Valoracion, self).save(*args, **kwargs)


    def toJSONValoracion(self):
        json = {'usuario': self.usuario.pk,
                'calidad': self.calidad,
                'espera': self.espera,
                'comida': self.comida,
                'valoracion_media': self.valoracion_media,
                'texto': self.texto,
                }
        return json


class ValoracionAbierta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, null=True,blank=True)
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE , null=True,blank=True)
    activa = models.BooleanField(default=False)
    fecha = models.DateTimeField(auto_now_add=True)
    fecha_fin = models.DateTimeField(blank=True,null=True)

    def __unicode__(self):
        return u"%s_%s_%s_%s" %(self.usuario, self.restaurante, self.activa, self.fecha)



class Favoritos(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, null=True, blank=True)
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE, null=True, blank=True)
    favorito = models.BooleanField(default=False)

    def __str__(self):
        return u"%s_%s" %(self.restaurante.nombre, self.usuario.username)

    def toJSONFavoritos(self):
        json = {'pk': self.restaurante.pk,
                }
        return json


class Alergenos(models.Model):
    nombre = models.CharField(max_length=300)
    nombre_slug = models.SlugField(blank=True, editable=False)

    def __str__(self):
        return u"%s" % self.nombre_slug

    def save(self, *args, **kwargs):
        self.nombre_slug = slugify(self.nombre)
        super(Alergenos, self).save(*args, **kwargs)

    def toJSONFavoritos(self):
        json = {'nombre': self.nombre,
                }
        return json


class CategoriaProducto(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=300)
    nombre_slug = models.SlugField(blank=True, editable=False)
    imagen = models.ImageField(upload_to='imagenes/CategoriaProducto/', blank=True, null=True)
    tipo_dieta = models.ForeignKey(TipoDieta, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return u"%s_%s" %(self.restaurante.nombre, self.nombre_slug)

    def save(self, *args, **kwargs):
        self.nombre_slug = slugify(self.nombre)
        super(CategoriaProducto, self).save(*args, **kwargs)

    def toJSONFavoritos(self):
        json = {'pk': self.restaurante.pk,
                }
        return json


class Producto(models.Model):
    categoria = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=300)
    nombre_slug = models.SlugField(blank=True, editable=False)
    imagen = models.ImageField(upload_to='imagenes/CategoriaProducto/', blank=True, null=True)
    descripcion = models.CharField(max_length=400)
    precio_base = models.IntegerField()
    precio_domicilio_extra = models.IntegerField()
    alergenos = models.ForeignKey(Alergenos, on_delete=models.CASCADE, blank=True,null=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return u"%s_%s" %(self.categoria.nombre, self.nombre_slug)

    def save(self, *args, **kwargs):
        self.nombre_slug = slugify(self.nombre)
        super(Producto, self).save(*args, **kwargs)

    def toJSONFavoritos(self):
        json = {'pk': self.categoria.pk,
                }
        return json


class Ingrediente(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=300)
    nombre_slug = models.SlugField(blank=True, editable=False)
    precio = models.IntegerField()
    alergenos = models.ForeignKey(Alergenos, on_delete=models.CASCADE, blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return u"%s_%s" %(self.producto.nombre, self.nombre_slug)

    def save(self, *args, **kwargs):
        self.nombre_slug = slugify(self.nombre)
        super(Ingrediente, self).save(*args, **kwargs)

    def toJSONFavoritos(self):
        json = {'pk': self.producto.pk,
                }
        return json


class Horario(models.Model):
    DIA_SEMANA = [('Lunes', 'lunes'),
              ('Martes', 'martes'),
              ('Miercoles', 'miercoles'),
              ('Jueves', 'jueves'),
              ('Viernes', 'viernes'),
              ('Sabado', 'sabado'),
              ('Domingo', 'domingo')]
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, null=True,blank=True)
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE , null=True,blank=True)
    dia_semana = models.CharField(max_length=50, choices=DIA_SEMANA)
    inicio = models.TimeField()
    fin = models.TimeField()
    fecha = models.DateTimeField(auto_now_add=True)
    cerrado = models.BooleanField(default=False)


    def __str__(self):
        return u"%s_%s" %(self.restaurante.nombre, self.dia_semana)

    def toJSONFavoritos(self):
        json = {'pk': self.restaurante.pk,
                }
        return json


class Cp(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    cp = models.CharField(max_length=5)
    inicio = models.TimeField()
    fin = models.TimeField()
    precio_reparto = models.IntegerField()
    coste_usuario = models.IntegerField()
    coste_restaurante = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)


    def __unicode__(self):
        return u"%s_%s" %(self.restaurante.nombre, self.cp)


    def save(self, *args, **kwargs):
        self.restaurante.coste_resparto_cliente = self.coste_usuario
        self.restaurante.save()
        super(Cp, self).save(*args, **kwargs)

    def toJSONFavoritos(self):
        json = {'pk': self.restaurante.pk,
                }
        return json


class HorarioReparto(models.Model):
    DIA_SEMANA = [('Lunes', 'lunes'),
              ('Martes', 'martes'),
              ('Miercoles', 'miercoles'),
              ('Jueves', 'jueves'),
              ('Viernes', 'viernes'),
              ('Sabado', 'sabado'),
              ('Domingo', 'domingo')]

    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    dia_semana = models.CharField(max_length=50, choices=DIA_SEMANA)
    inicio = models.TimeField()
    fin = models.TimeField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return u"%s_%s" % (self.restaurante.nombre, self.dia_semana)

    def toJSONFavoritos(self):
        json = {'pk': self.restaurante.pk,
                }
        return json


class DiaFestivo(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, null=True,blank=True)
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE , null=True,blank=True)
    inicio = models.DateField()
    numero_dias = models.IntegerField()
    descripcion = models.CharField(max_length=300)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return u"%s_%s" %(self.restaurante.nombre, self.descripcion)

    def toJSONFavoritos(self):
        json = {'pk': self.restaurante.pk,
                }
        return json

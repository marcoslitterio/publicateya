from django.db import models

class Localidad(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre

class Cliente(models.Model):
    razon_social = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200,blank=True, null=True)
    direccion = models.CharField(max_length=200, null=True)
    cuit = models.BigIntegerField(null=True)
    localidad = models.ForeignKey(Localidad, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    contacto = models.CharField(max_length=200, blank=True, null=True)
    telefono_a = models.CharField(max_length=20, blank=True, null=True)
    contacto_a = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=70, blank=True, null=True, unique=True)
        
    def __unicode__(self):
        return self.razon_social


class Pantalla(models.Model):
    direccion = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)

        
    def __unicode__(self):
        return str(self.descripcion)

class Propaganda(models.Model):
    descripcion = models.CharField(max_length=200)
    duracion = models.TimeField()
    cliente_id = models.ForeignKey(Cliente)
    video_propio = models.BooleanField(default=False)
    
    def __unicode__(self):
        return str(self.descripcion)


class Bucle(models.Model):
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    pantalla = models.ForeignKey(Pantalla)
    propagandas = models.ManyToManyField(Propaganda)
            
    def __unicode__(self):
        return str(self.id)

class TipoFactura(models.Model):
    descripcion = models.CharField(max_length=2)

    def __unicode__(self):
        return str(self.descripcion)

class Factura(models.Model):
    numero_factura = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente)
    tipo_factura = models.ForeignKey(TipoFactura)
    fecha = models.DateField()

    def __unicode__(self):
        return str(self.numero_factura)

class DetalleFactura(models.Model):
    factura = models.ForeignKey(Factura)
    importe = models.FloatField()
    descripcion = models.CharField(max_length=200)    

    
        

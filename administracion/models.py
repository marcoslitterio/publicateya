from django.db import models

class Cliente(models.Model):
    razon_social = models.CharField(max_length=200)
        
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

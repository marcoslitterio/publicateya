from django.contrib import admin
from administracion.models import *

#from django.conf.urls.defaults import patterns

 
admin.site.register(Pantalla)
admin.site.register(Propaganda)
admin.site.register(Cliente)
admin.site.register(TipoFactura)
admin.site.register(Localidad)

#-----------------------------------------------
class DetalleFacturaInLine(admin.TabularInline):
    model = DetalleFactura

class FacturaAdmin(admin.ModelAdmin):
    inlines = [
        DetalleFacturaInLine,
    ]
admin.site.register(Factura, FacturaAdmin)
#-----------------------------------------------
class BucleAdmin(admin.ModelAdmin):
    filter_horizontal = ("propagandas",)
admin.site.register(Bucle, BucleAdmin)
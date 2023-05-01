from django.contrib import admin

# Register your models here.

from .models import Registro,Poll ,Choice ,Region ,Provincia ,Comuna ,Persona ,Sucursal ,Cargo , Empleado ,Postres , Catalogos  ,Cafe ,Tamanio ,CafeTam ,FormaPago , Agregado ,Pedido 

admin.site.register(Registro)
admin.site.register(Poll )
admin.site.register(Choice )
admin.site.register(Region )
admin.site.register(Provincia )
admin.site.register(Comuna )
admin.site.register(Persona )
admin.site.register(Sucursal )
admin.site.register(Cargo ) 
admin.site.register(Empleado )
admin.site.register(Postres ) 
admin.site.register(Catalogos ) 
admin.site.register(Cafe )
admin.site.register(Tamanio )
admin.site.register(CafeTam )
admin.site.register(FormaPago ) 
admin.site.register(Agregado )
admin.site.register(Pedido )

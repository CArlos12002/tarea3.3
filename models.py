from django.db import models

# Create your models here.
from django.db import models
"""
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
"""
##  Tablas generalmente en ejercicios
##  como no tiene Meta(db_table), 
##   todas quedan con un prefijo
class Poll(models.Model):
    # No Tiene ID, es automático
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    # No tiene Id, es automático
    # Observe la FK, obligación => on_delete
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    # Integer
    votes = models.IntegerField(default=0)

########################


class Region(models.Model):# steve
    id_reg =models.AutoField(primary_key=True)
    cod_region = models.IntegerField(null=False)
    nombre = models.CharField(max_length= 30)
    def __str__(self):
        return self.nombre
    class Meta:
    	db_table = 'db_region'

class Provincia(models.Model):
    id_prov =models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    id_region = models.ForeignKey(Region, on_delete=models.CASCADE)
    class Meta:
    	db_table = 'db_provincia'


class Comuna(models.Model):
    id_com =models.AutoField(primary_key=True)
    cod_comuna = models.CharField(max_length= 10, default="")
    id_provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    nombre = models.TextField(max_length= 30)
    def __str__(self):
        return self.nombre
    class Meta:
    	db_table = 'db_comuna'

class Persona(models.Model):
    rut = models.IntegerField(null=False, primary_key=True)
    dv = models.CharField(max_length=1, null=False)
    nombre = models.CharField(max_length=20)
    papellido = models.CharField(max_length=20)
    sapellido = models.CharField(max_length=20)
    contacto = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    id_comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.rut
    #nombre + ' ' + self.papellido
    class Meta:
    	db_table = 'db_persona'

class Sucursal(models.Model):
    id_suc =models.AutoField(primary_key=True)
    id_comuna = models.ForeignKey(Comuna,on_delete=models.CASCADE,default=0)
    cod_sucursal = models.CharField(max_length=10)
    direccion = models.TextField(default=0)
    
    def __str__(self):
        return self.direccion
    class Meta:
    	db_table = 'db_sucursal'

class Cargo(models.Model): #steve
    id_car =models.AutoField(primary_key=True)
    codCargo = models.IntegerField(null=False)
    nombre = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.nombre
    class Meta:
    	db_table = 'db_cargo'

class Empleado(models.Model):
    rut_id = models.AutoField(primary_key=True)  
    #  observe en la base de datos queda cargo_id
    cargo = models.ForeignKey(Cargo,on_delete=models.CASCADE,default=0)
    sueldo = models.CharField(max_length=200, null=False)
    sucursal = models.ForeignKey(Sucursal,on_delete=models.CASCADE,default=0)
    rut_persona = models.ForeignKey(Persona,on_delete=models.CASCADE,default=0)
    
    def __str__(self):
        return self.rut
    class Meta:
    	db_table = 'db_empleado'

###################
# Imagenes => python -m pip install Pillow

class Postres(models.Model): #steve
    nombre = models.CharField(max_length=100, default='')
    precio = models.CharField(max_length=20, default='')
    stock = models.CharField(max_length=100, default='')
    # upload_to   donde quedaran las imagenes
    img = models.ImageField(default='null',upload_to="fotosPostres")#upload_to='fotosImg'
    #  fecha del momento
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    class Meta:
         db_table = 'db_postres' # Le doy de nombre 'postres' a nuestra tabla en la Base de Datos

class Catalogos(models.Model): #steve
    nombre = models.CharField(max_length=100, default='')
    imgCatalogo = models.ImageField(default='null',upload_to="fotosPostres")#upload_to='fotosImg'
 
    class Meta:
         db_table = 'db_catalogo' # Le doy de nombre 'postres' a nuestra tabla en la Base de Datos

###################

# Create your models here.
class Registro(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    #   auto_now_add  fecha actual
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    clave = models.CharField(max_length=10)

    def __str__(self):
        return self.email

    class Meta:
    	db_table = 'db_registro'

class Cafe(models.Model):
    codCafe = models.IntegerField(null=False, primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    class Meta:
    	db_table = 'db_cafe'
class Tamanio(models.Model):
    codTamano = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre
    class Meta:
    	db_table = 'db_tamano'    

class CafeTam(models.Model):
    tamano = models.CharField(max_length=50)
    codTamano = models.CharField(max_length=40)
    codCafe = models.OneToOneField(Cafe, on_delete=models.PROTECT)

    def __str__(self):
        return self.tamaño

    class Meta:
    	db_table = 'db_cafetam'

class FormaPago(models.Model): #steve
    codFormaPago = models.IntegerField(null=False, primary_key=True)
    descripcion = models.CharField(max_length=200, null=False)
    
    def __str__(self):
        return self.descripcion
    class Meta:
    	db_table = 'db_formapago'

class Agregado(models.Model):
    codAgregados = models.IntegerField(null=False, primary_key=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
    	db_table = 'db_agregado'




class Pedido(models.Model):
    fechaPedido = models.DateField('Fecha de compra')
    descripcion = models.CharField(max_length=100)
    direccion = models.TextField(max_length=200)
    codFormaPago = models.OneToOneField(FormaPago, on_delete=models.PROTECT)
    rut = models.OneToOneField(Persona, on_delete=models.PROTECT)

    def __str__(self):
        return self.numPedido
    class Meta:
    	db_table = 'db_pedido'





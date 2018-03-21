from django.db import models


class Marca(models.Model):
	modelo 		= models.CharField(max_length =100)
	def __str__(self):
		return self.modelo

		
class Campeonato(models.Model):
	categoria 	= models.CharField(max_length = 50)
	fecha 		= models.DateTimeField()
	def __str__(self):
		return self.categoria

class Nacionalidad(models.Model):
	pais_origen =  models.CharField(max_length =100)

	def __str__(self):
		return self.pais_origen
		


class Piloto(models.Model):
	documento 		= models.IntegerField()
	nombres 		= models.CharField(max_length =200)
	apelidos 		= models.CharField(max_length =200)
	equipo			= models.CharField(max_length =100)
	nacionalidad	= models.ForeignKey(Nacionalidad, on_delete=models.CASCADE)
	campeonatos		= models.ManyToManyField(Campeonato, null = True, blank = True)
	
	def __str__(self):
		return self.nombres 

class Moto(models.Model):
	numero		= models.IntegerField ()
	cilindraje 	= models.CharField(max_length =100)
	color		= models.CharField(max_length = 50)
	categorias	= models.ForeignKey(Piloto, on_delete=models.CASCADE)
	marca		= models.ForeignKey(Marca, on_delete=models.CASCADE)
	
	def __str__(self):
		return str(self.numero)

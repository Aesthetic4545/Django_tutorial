from django.db import models

# Create your models here.


# tablas que se crean para importarlas a la base de datos
class Book(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    

    #metodo para mostrar en el admin el nombre del modelo
    def __str__(self):

        title = str(self.title) 
        author = str(self.author)


        return title + ' - ' + author
    

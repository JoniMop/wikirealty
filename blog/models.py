from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    #creo la tabla user en donde va registrando os usuarios
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


#Abajo creo funcion para que el dia en que se crea y el dia en que se publica puedan ser diferentes
    def publish(self):
        self.published_date = timezone.now()
        self.save()


#represento todo lo creado en string
    def __str__(self):
        return self.title


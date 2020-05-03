from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class News(models.Model):
    title = models.CharField( max_length=100)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    avtor = models.ForeignKey(User, verbose_name="Автор", on_delete=models.CASCADE)

    class Meta:
        managed = True
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("news-detail", kwargs={"pk": self.pk})
    


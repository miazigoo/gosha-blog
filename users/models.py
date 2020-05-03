from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    img = models.ImageField(default='default.jpg', upload_to='user_images', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return f'Профиль пользователя: {self.user.username}'
    
    def save(self, *args, **kwargs):
        super().save()

        image = Image.open(self.img.path)
        if image.height > 256 or image.width > 256:
            resize = (256, 256)
            image.thumbnail(resize)
            image.save(self.img.path)

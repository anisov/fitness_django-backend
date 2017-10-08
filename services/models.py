from django.db import models
# Create your models here.


class ServicesModel(models.Model):
    img = models.ImageField(upload_to='img', blank=False, null=True, verbose_name='Фото услуги',
                            default='', validators=[])
    title = models.CharField(verbose_name='Заголовок', max_length=128, null=False, blank=False)
    text = models.TextField(verbose_name='Заголовок', null=False, blank=False)

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'Услуги'
        verbose_name_plural = "Услуги"

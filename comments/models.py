from django.db import models
from datetime import datetime
class Comment_post(models.Model):
    name = models.CharField(null=True,max_length=200,verbose_name = 'Имя')
    vk_url = models.URLField(null=True,max_length=250)
    img = models.ImageField(upload_to='img', blank=True, null=True, verbose_name='Фото')
    text = models.TextField(null=True, verbose_name = 'Комментарий')
    pub_date = models.DateTimeField('Дата комментария', default=datetime.now())
    approved_comment = models.BooleanField(default=True)
    ip_address = models.GenericIPAddressField(default='127.1.0.1', verbose_name='ip')

    def __str__(self):
        return  self.name

    class Meta():
        verbose_name = 'Коментарии'
        verbose_name_plural = "Коментарии"


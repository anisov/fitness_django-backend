from django.db import models
from datetime import datetime
import os
from django.core.exceptions import ValidationError


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf', '.doc', '.docx', '.jpg', '.png', '.xlsx', '.xls']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')


class CommentPost(models.Model):
    name = models.CharField(null=False,max_length=200,verbose_name = 'Имя')
    vk_url = models.URLField(null=False,max_length=250)
    img = models.ImageField(upload_to='img', blank=True, null=False, verbose_name='Фото',default='/img/comments/vector-smart-object.png', validators=[validate_file_extension])
    img_on = models.BooleanField(default=True)
    text = models.TextField(null=False, verbose_name = 'Комментарий')
    pub_date = models.DateTimeField('Дата комментария', default=datetime.now())
    approved_comment = models.BooleanField(default=True)
    ip_address = models.GenericIPAddressField(default='127.1.0.1', verbose_name='ip')

    def __str__(self):
        return  self.name

    class Meta():
        verbose_name = 'Коментарии'
        verbose_name_plural = "Коментарии"


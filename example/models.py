from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    phone = models.CharField(max_length=200, verbose_name='Номер телефона')

    def __str__(self):
        # Будет отображаться следующее поле в панели администрирования
        return self.name
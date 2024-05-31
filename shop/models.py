from django.db import models

class Order(models.Model):

    STATUSORDER_CHOICES = [
        ('Выполнен', 'Выполнен'),
        ('В работе', 'В работе'),
        ('Новый', 'Новый'),
    ]

    klient = models.CharField(max_length=500, verbose_name='Клиент')
    number = models.CharField(max_length=500, verbose_name='Номер заказчика')
    email = models.EmailField(max_length=500, verbose_name='Почта')
    address = models.CharField(max_length=500, verbose_name='Адрес')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')
    status = models.CharField(choices=STATUSORDER_CHOICES, verbose_name='Статус заказа')
from django.db import models

class Partner(models.Model):
    partner_type = models.CharField(max_length=255)
    partner_name = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    address = models.TextField(verbose_name='юридический адресс')
    inn = models.CharField(max_length=12)
    rating = models.PositiveIntegerField(verbose_name='рейтинг')

    def __str__(self):
        return self.partner_name
    
class Product(models.Model):
    product_type = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    article = models.CharField(max_length=10)
    min_price = models.FloatField(verbose_name='минимальная стоимость')

    def __str__(self):
        return self.product_name
    
class Sale(models.Model):
    name_product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    name_partner = models.ForeignKey(Partner, on_delete=models.CASCADE, verbose_name='партнер')
    quantity = models.CharField(max_length=20)
    date_sale = models.DateField(verbose_name='дата продажи')

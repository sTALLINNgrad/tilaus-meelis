from django.db import models

class Category(models.Model):            # product_set will be automatically created
    name = models.TextField(max_length=100)

    def __str__(self):
        return self.name

class Tuotesarja(models.Model):
    name = models.TextField(max_length=100)

    def __str__(self):
        return self.name

class Toimittaja(models.Model):
    name = models.TextField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    s_numero = models.CharField(max_length=7)
    category = models.ForeignKey(Category,  on_delete = models.PROTECT)
    tuotesarja = models.ForeignKey(Tuotesarja, on_delete = models.PROTECT)
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    toimittajan_tuotekoodi = models.CharField(max_length=20)
    toimittaja = models.ForeignKey(Toimittaja, on_delete = models.PROTECT)
    
    kuva = models.ImageField(upload_to='products/img/%Y/%m/%d')  # Поле для загрузок картинок товаров
    
    
    def __str__(self):
        return self.name
    
    
    
   
class Image(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title 
       

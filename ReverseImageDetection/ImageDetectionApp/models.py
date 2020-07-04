from django.db import models


class TopAndTshirt(models.Model):
    image_url=models.URLField(verbose_name="Image URL Field")
    product_url=models.URLField(verbose_name="Product URL")
    brand_name=models.CharField(verbose_name='Brand Name', max_length=450)
    product_name=models.CharField(verbose_name='Product Name', max_length=550)
    price=models.IntegerField(verbose_name="Product Price")

class Trouser(models.Model):
    image_url=models.URLField(verbose_name="Image URL Field")
    product_url=models.URLField(verbose_name="Product URL")
    brand_name=models.CharField(verbose_name='Brand Name', max_length=450)
    product_name=models.CharField(verbose_name='Product Name', max_length=550)
    price=models.IntegerField(verbose_name="Product Price")

class Pullover(models.Model):
    image_url=models.URLField(verbose_name="Image URL Field")
    product_url=models.URLField(verbose_name="Product URL")
    brand_name=models.CharField(verbose_name='Brand Name', max_length=450)
    product_name=models.CharField(verbose_name='Product Name', max_length=550)
    price=models.IntegerField(verbose_name="Product Price")

class Dress(models.Model):
    image_url=models.URLField(verbose_name="Image URL Field")
    product_url=models.URLField(verbose_name="Product URL")
    brand_name=models.CharField(verbose_name='Brand Name', max_length=450)
    product_name=models.CharField(verbose_name='Product Name', max_length=550)
    price=models.IntegerField(verbose_name="Product Price")

class Coat(models.Model):
    image_url=models.URLField(verbose_name="Image URL Field")
    product_url=models.URLField(verbose_name="Product URL")
    brand_name=models.CharField(verbose_name='Brand Name', max_length=450)
    product_name=models.CharField(verbose_name='Product Name', max_length=550)
    price=models.IntegerField(verbose_name="Product Price")

class Sandal(models.Model):
    image_url=models.URLField(verbose_name="Image URL Field")
    product_url=models.URLField(verbose_name="Product URL")
    brand_name=models.CharField(verbose_name='Brand Name', max_length=450)
    product_name=models.CharField(verbose_name='Product Name', max_length=550)
    price=models.IntegerField(verbose_name="Product Price")

class Shirt(models.Model):
    image_url=models.URLField(verbose_name="Image URL Field")
    product_url=models.URLField(verbose_name="Product URL")
    brand_name=models.CharField(verbose_name='Brand Name', max_length=450)
    product_name=models.CharField(verbose_name='Product Name', max_length=550)
    price=models.IntegerField(verbose_name="Product Price")

class Sneaker(models.Model):
    image_url=models.URLField(verbose_name="Image URL Field")
    product_url=models.URLField(verbose_name="Product URL")
    brand_name=models.CharField(verbose_name='Brand Name', max_length=450)
    product_name=models.CharField(verbose_name='Product Name', max_length=550)
    price=models.IntegerField(verbose_name="Product Price")

class Bag(models.Model):
    image_url=models.URLField(verbose_name="Image URL Field")
    product_url=models.URLField(verbose_name="Product URL")
    brand_name=models.CharField(verbose_name='Brand Name', max_length=450)
    product_name=models.CharField(verbose_name='Product Name', max_length=550)
    price=models.IntegerField(verbose_name="Product Price")

class AnkleBoot(models.Model):
    image_url=models.URLField(verbose_name="Image URL Field")
    product_url=models.URLField(verbose_name="Product URL")
    brand_name=models.CharField(verbose_name='Brand Name', max_length=450)
    product_name=models.CharField(verbose_name='Product Name', max_length=550)
    price=models.IntegerField(verbose_name="Product Price")

from django.db import models
from django.urls import reverse


# Create your models here.
class category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField()
    image=models.ImageField(upload_to='cat')
    class Meta:
        ordering=('name',)
        verbose_name='name'
        verbose_name_plural='categorys'

    def get_url(self):
        return reverse('flipkartapp:products_by_category',args=[self.slug])



    def __str__(self):
        # return '{}'.format(self.name)
        return str(self.name)

class product(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField()
    image=models.ImageField(upload_to='product',blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('flipkartapp:prodCatdetail',args=[self.category.slug,self.slug])

    class Meta:
        ordering=('name',)
        verbose_name='product'
        verbose_name_plural='products'
        def __str__(self):
            # return '{}'.format(self.name)
            return str(self.name)

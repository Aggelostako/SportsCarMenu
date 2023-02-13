from django.db import models


class Item(models.Model):
    item_brand = models.CharField(max_length=200,null=True)
    item_name = models.CharField(max_length=200,null=True)
    item_desc = models.CharField(max_length=200,null=True)
    item_color = models.CharField(max_length=200,null=True)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500,default ="https://www.willow-car-sales.co.uk/wp-content/uploads/2019/11/placeholder-image-1.jpg")


    def __str__(self) :
        return f'{self.item_name}  {self.item_brand}'




# Create your models here.

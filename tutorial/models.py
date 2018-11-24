from django.db import models
from django.db.models import CharField
from django.contrib import admin

class Sensor(models.Model):
    # class Meta:
    # managed=False
    # db_table='TBL1'
    SensorNo = models.IntegerField(primary_key=True)
    SensorStatus = models.IntegerField()



class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    supplier_name = models.CharField(max_length=200)

    def __str__(self):
        return self.supplier_name

class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    article_label = models.CharField(max_length=200)
    article_sensor_no = models.IntegerField()
    article_sensor_status = models.BooleanField(default="True")
    article_supplier = models.ManyToManyField(Supplier)#, through='Detail')

    def __str__(self):
        return self.article_label

class Detail(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    shipment_cost = models.IntegerField()
    order_min = models.IntegerField()

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    order_article = models.ForeignKey(Article, on_delete=models.CASCADE)
    order_number = models.CharField(max_length=200)
    order_date = models.DateField()





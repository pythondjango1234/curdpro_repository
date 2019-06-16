from django.db import models
class ProductData(models.Model):
    Product_Id=models.IntegerField()
    Product_Name=models.CharField(max_length=100)
    Product_Cost=models.IntegerField()
    Product_Color=models.CharField(max_length=100)
    Product_Class=models.CharField(max_length=100)
    Customer_Name=models.CharField(max_length=100)
    Customer_Mobile=models.BigIntegerField()
    Customer_Email=models.EmailField()

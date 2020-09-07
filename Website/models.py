from django.db import models
#Creating models (Table)
class Product(models.Model):                                              #Inheritance is used

    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50, default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()
    image=models.ImageField(upload_to="images",default="")

    def __str__(self):
     return self.product_name               #to show the name of object after adding e.g Ghadi,Fastrack watch ....before this product object(1)..is shown

class Contact(models.Model):

        message_id = models.AutoField(primary_key=True)
        name = models.CharField(max_length=50)
        email = models.CharField(max_length=50, default="")
        phone = models.CharField(max_length=10, default="")
        desc = models.CharField(max_length=500, default="")

        def __str__(self):
            return self.name  # to show the name of object after adding e.g Ghadi,Fastrack watch ....before this product object(1)..is shown
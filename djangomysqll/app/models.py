from django.db import models

class Customer(models.Model):
    CITIES = (
        ('Noida', 'Noida'),
        ('Lucknow', 'Lucknow')
    
    )
    
    
    customer=models.CharField(max_length=200)
    address1=models.TextField()
    email=models.EmailField(max_length=200,unique=True)
    landline_no=models.CharField(max_length=15) 
    contact_person=models.CharField(max_length=200)
    
    city = models.CharField(max_length=18, choices=CITIES)
    address2=models.TextField()
    mobile=models.CharField(max_length=15)
    gstno=models.CharField(max_length=15)
    
    class Meta:
        db_table='customtb'
from django.db import models

# Create your models here.

class User(models.Model):
    # id : models.IntegerField() removing id because in in <python make makemigrations> cmnd it will automaticaly created
    email  = models.EmailField()
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    mobile_no = models.BigIntegerField()
    user_id =models.AutoField(primary_key=True)



class Customer(models.Model):
    # id : models.IntegerField() removing id because in in <python make makemigrations> cmnd it will automaticaly created
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_number = models.BigIntegerField()


    
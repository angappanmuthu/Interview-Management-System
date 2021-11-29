from django.db import models

# Create your models here.

class MobileVerification(models.Model):
    mobile = models.IntegerField()
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

class EmailVerification(models.Model):
    mobile = models.CharField(max_length=100)
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

class State(models.Model):
    state = models.CharField(max_length=50)

    def __str__(self):
        return str(self.state)

class District(models.Model):
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    district = models.CharField(max_length=100)

    def __str__(self):
        return str(self.district)

class City(models.Model):
    district = models.ForeignKey(District,on_delete=models.CASCADE)
    city = models.CharField(max_length=100)

    def __str__(self):
        return str(self.city)

class Pincode(models.Model):
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    pincode = models.IntegerField()

    def __str__(self):
        return str(self.pincode)

class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    mobile = models.ForeignKey(MobileVerification,on_delete=models.CASCADE)
    email = models.EmailField()
    address = models.TextField()
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    district = models.ForeignKey(District,on_delete=models.CASCADE)
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    pincode = models.ForeignKey(Pincode,on_delete=models.CASCADE)

class PanelMember(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    mobile = models.ForeignKey(MobileVerification,on_delete=models.CASCADE)
    email = models.EmailField()
    address = models.TextField()
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    district = models.ForeignKey(District,on_delete=models.CASCADE)
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    pincode = models.ForeignKey(Pincode,on_delete=models.CASCADE)

class PanelAdmin(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    mobile = models.ForeignKey(MobileVerification,on_delete=models.CASCADE)
    email = models.EmailField()
    address = models.TextField()
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    district = models.ForeignKey(District,on_delete=models.CASCADE)
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    pincode = models.ForeignKey(Pincode,on_delete=models.CASCADE)

class Company(models.Model):
    company = models.CharField(max_length=100)

class Post(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    post = models.CharField(max_length=100)

class Interview(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
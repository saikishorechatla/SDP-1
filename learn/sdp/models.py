from django.db import models
from django.db import models
# Create your models here.
import datetime
import os

#Create your models here.
class movie(models.Model):
    username = models.CharField(max_length=200)
    business= models.CharField(max_length=200)
    name= models.CharField(max_length=200)
    thadd= models.CharField(max_length=200)
    city= models.CharField(max_length=200)
    zip= models.CharField(max_length=200)
    price= models.CharField(max_length=200)
    yaddress= models.CharField(max_length=200)
    ycity= models.CharField(max_length=200)
    yzip= models.CharField(max_length=200)
    phnum= models.CharField(max_length=200)
    email= models.CharField(max_length=200)

class cat(models.Model):
    username=models.CharField(max_length=200)
    sname = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    pph = models.CharField(max_length=200)
    capacity=models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def str(self):
        return ' Name : ' + self.name + ' - Event : ' + self.sname
class music(models.Model):
    username = models.CharField(max_length=200)
    conname=models.CharField(max_length=200)
    nameor=models.CharField(max_length=200)
    conadd=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    zip=models.CharField(max_length=200)
    price=models.CharField(max_length=200)
    yaddress=models.CharField(max_length=200)
    ycity=models.CharField(max_length=200)
    yzip=models.CharField(max_length=200)
    phno=models.CharField(max_length=200)
    email=models.CharField(max_length=200)

class marriage(models.Model):
    username=models.CharField(max_length=200)
    hall1=models.CharField(max_length=200)
    halladd1=models.CharField(max_length=200)
    city1=models.CharField(max_length=200)
    zip1=models.CharField(max_length=200)
    pricepe1=models.CharField(max_length=200)
    capacity1=models.CharField(max_length=200)
    phno1=models.CharField(max_length=200)
    email1=models.CharField(max_length=200)

class contactf(models.Model):
    username=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    problem=models.CharField(max_length=600)
class dcontactf(models.Model):
    username=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    problem=models.CharField(max_length=600)
class addmovies(models.Model):
    username=models.CharField(max_length=200)
    theatrename=models.CharField(max_length=200)
    moviename=models.CharField(max_length=200)
    genre=models.CharField(max_length=200)
    theatreaddress=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    zip=models.CharField(max_length=200)
class event(models.Model):
    username=models.CharField(max_length=200)
    Typeofevent=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    date=models.CharField(max_length=200)
    starttime=models.CharField(max_length=200)
    endtime=models.CharField(max_length=200)
    venue=models.CharField(max_length=200)
    isfood=models.CharField(max_length=200)
class moviepic(models.Model):
    avatar = models.ImageField(upload_to='uploads/')
class addmovies2(models.Model):
    # username=models.CharField(max_length=200)
    theatrename=models.CharField(max_length=200)
    moviename=models.CharField(max_length=200)
    genre=models.CharField(max_length=200)
    theatreaddress=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    zip=models.CharField(max_length=200)
    poster=models.ImageField(upload_to='uploads/')


def __str__(self):
    return self.title
def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)

class Item(models.Model):
    name = models.CharField(max_length=191)
    mname= models.CharField(max_length=191)
    genre=models.CharField(max_length=191)
    thaddress = models.CharField(max_length=500, null=True)
    capacity=models.CharField(max_length=50)
    image = models.ImageField(upload_to=filepath, null=True, blank=True)
    video = models.FileField(upload_to=filepath, null=True, blank=True)











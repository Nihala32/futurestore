from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.

class Blogs(models.Model):
    title=models.CharField(max_length=50)
    content=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    liked_by=models.ManyToManyField(User,max_length=50)

    def __str__(self):
        return self.title

class Mobiles(models.Model):
    name=models.CharField(max_length=120,unique=True)
    price=models.PositiveIntegerField(default=5000)
    band=models.CharField(max_length=120,default="4g")
    display=models.CharField(max_length=120)
    processor=models.CharField(max_length=120)

    def __str__(self):
        return self.name

    def average_rating(self):
        reviews=self.reviews_set.all()
        if reviews:
            rating=[rv.rating for rv in reviews]
            total=sum(rating)
            return total/len(reviews)
        else:
            return 0

    def total_reviews(self):
        return self.reviews_set.all().count()



class Reviews(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Mobiles,on_delete=models.CASCADE)
    review=models.CharField(max_length=120)
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    date=models.DateField(auto_now_add=True)

    class Meta:
        unique_together=("author","product")

    def __str__(self):
        return self.review


class Carts(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Mobiles,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    options=(
        ("incart","incart"),
        ("order-placed","order-placed"),
        ("cancelled","cancelled")
    )
    status=models.CharField(max_length=120,choices=options,default="incart")


class Orders(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE),
    product=models.ForeignKey(Mobiles,on_delete=models.CASCADE)
    options=(
        ("order-placed",'order-placed'),
        ('dispatched','dispatched'),
        ('cancelled','cancelled'),
        ('delivered','delivered')
         )
    status=models.CharField(max_length=120,choices=options,default="order-placed")




# orm query for creating a resourse
# modelname.objects.create(fieldname=aa)

# orm query for fetching all objects
# modelname.objects.all()
# qs=blogs.objects.all()

# detailview of a specific object
# qs=modelname.objects.get(id=1)





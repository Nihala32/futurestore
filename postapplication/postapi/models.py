from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Userprofile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    dob=models.DateField(null=True)
    options=(
        ("male","male"),
        ("female","female")
    )
    gender=models.CharField(max_length=20,choices=options)
    profile_pic=models.ImageField(upload_to="profilepictures",null=True)
    bio=models.CharField(max_length=120)
    cover_pic=models.ImageField(upload_to="coverpic",null=True)
    followings=models.ManyToManyField(User,related_name="following",null=True)







class Posts(models.Model):
    title=models.CharField(max_length=120)
    content=models.CharField(max_length=120)
    image=models.ImageField(upload_to="postimages",null=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateField(auto_now_add=True)
    liked_by=models.ManyToManyField(User,related_name="liked_by")

    def __str__(self):
        return self.title


    def fetch_comments(self):
        return self.comments_set.all()

    def like_count(self):
        return self.liked_by.all().count()


class Comments(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.CharField(max_length=120)
    post=models.ForeignKey(Posts,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.comment



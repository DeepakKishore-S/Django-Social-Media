from PIL import Image
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.urls import reverse
# Create your models here.




class Post(models.Model):
    title = models.CharField(max_length=30)
    subject = models.CharField(max_length=100, default=' ')
    content = models.TextField(blank=True)
    pic = models.ImageField(default='default.jpg',upload_to='post_pics', blank=True)
    like = models.ManyToManyField(User,blank=True,related_name='post_likes')
    favourite = models.ManyToManyField(User, blank=True, related_name='post_favourites')
    date_posted = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    Comment = models.CharField(max_length=100000)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Comment


GENDER_CHOICES = (
   ('Male', 'Male'),
   ('Female', 'Female'),
    ('Others', 'Others')
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(default=' ', blank=True, max_length=12)
    Profile_image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    Interested_in = models.CharField(default=' ',blank=True, max_length=80)
    Follower = models.ManyToManyField(User,related_name='Follower')
    Following = models.ManyToManyField(User,blank=True,related_name='Following')
    gender = models.CharField(choices=GENDER_CHOICES, max_length=128, default='Male')
    dob = models.DateField(max_length=8, blank=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.Profile_image.path)

        if img.height >300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.Profile_image.path)

    def get_absolute_url(self):
        return reverse('userpage', kwargs={'id': self.pk})




def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile=Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile,sender=User)


from django.db import models

# Create your models here.
class TwitterUser(models.Model):
    twitter_user= models.CharField(max_length=30)

    def __str__(self):
        return self.twitter_user

class Track(models.Model):
    user= models.ForeignKey('podcast_app.TwitterUser', on_delete=models.CASCADE)
    track= models.URLField(max_length=100)
    def __str__(self):
        return self.track

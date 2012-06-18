from django.db import models
from django.contrib.auth.models import User
#import string
#import random
#import hashlib

# Create your models here.

def rnd_str(rnd_len = 6):
    import string, random
    
    choice_set = string.ascii_letters + string.digits
    return "".join([random.choice(choice_set) for i in range(rnd_len)])


class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
        
    def __unicode__(self):
        return u"(%.8f; %.8f)" %(self.latitude, self.longitude)
        
    
class Quest(models.Model):
    quest_type = models.CharField(max_length = 20)
    
    def __unicode__(self):
        return self.quest_type
        
        
class Permissions(models.Model):
    name = models.CharField(max_length = 20)
    
    def __unicode__(self):
        return self.name


class Artifact(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField(blank = True)
    uid = models.CharField(max_length = 16, unique = True, 
                                db_index = True)
                                
    photo = models.ImageField(upload_to = "/gifts/photos", blank = True)
    creators = models.ManyToManyField(User, related_name = 'created_gifts') #origin created the gift
    masters = models.ManyToManyField(User, related_name = 'mastered_gifts') #master has rights and ratings of the gift
    owner = models.ForeignKey(User, related_name = 'owned_gifts') #owner is person, who has got the gift by last transaction
    create_datetime = models.DateTimeField(auto_now_add=True)
    create_location = models.ForeignKey(Location, blank=True, null=True, related_name = '+') #location field type will be specified after learning geolocation
    lastpass_datetime = models.DateTimeField(blank=True, null=True) #not required. It's possible to get it from transactions 
    lastpass_location = models.ForeignKey(Location, blank=True,  null=True, related_name = '+') #may be obtained from transactions + location type = ?    
    quest = models.ForeignKey(Quest, blank=True, null=True, related_name = '+')
    permissions = models.ForeignKey(Permissions, related_name = '+')
    ratings = models.IntegerField(default=0)
    abuses = models.IntegerField(default=0)
    status = models.IntegerField(default=1)
    
    def __unicode__(self):
        return self.name
        

        

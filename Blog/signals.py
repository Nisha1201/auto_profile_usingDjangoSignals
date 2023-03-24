from django.db.models.signals import post_save, pre_delete,pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
# from django.contrib.auth import get_user_model

# User=get_user_model()
 
 
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print(sender,"sender-------------")
    print(instance,"instance------------")
    print(created,"created-------------")
    print(f"kwargs:{kwargs}-------------")
    if created:
        Profile.objects.create(user=instance)
        # instance.profile.save()





  
# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#         instance.profile.save()

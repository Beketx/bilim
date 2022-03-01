"""
There are 3 types of signal.

pre_save/post_save: This signal  works before/after the method save().
pre_delete/post_delete: This signal  works before after delete a model’s instance (method delete()) this signal is thrown.
pre_init/post_init: This signal is thrown before/after instantiating a model (__init__() method).
"""

# POST_SAVE
from django.db.models.signals import post_save, pre_delete
# from django.contrib.auth.models import User
# from django.dispatch import receiver
# from .models import Profile
 
 
# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
  
# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#         instance.profile.save()

"""
receiver – The function who receives the signal and does something.
sender – Sends the signal
created — Checks whether the model is created or not
instance — created model instance
**kwargs –wildcard keyword arguments
"""

#-----------------------------------

"""
Pre_save method is provoked just before the save function is called,
Also the model is saved only after successful execution of pre_save method
"""
# PRE_SAVE
# from django.db.models.signals import post_save, pre_delete,pre_save
# from django.contrib.auth.models import User
# from django.dispatch import receiver
# from .models import Profile
 
 
# @receiver(pre_save, sender=User)
# def checker(sender, instance, **kwargs):
#     if instance.id is None:
#         pass
#     else:
#       current=instance
#       previous=User.objects.get(id=instance.id)
#       if previous.reaction!= current.reaction:
#                #save method can be called
"""
We use this if  reaction is changed.

Using signals Connect Method

The alternative way of above method is to use connect method to fire signals.

If you just use post_save.connect(my_function), then it will get fired as soon as any save method is fired.

post_save.connect(my_function_post_save, sender=MyModel)
pre_save.connect(my_function, sender= UserTextMessage)
"""

#-----------------------------------


"""
Another way to connect the signal with the function:

You need to connect the signals file with the app.py
file ready function in order to use them.
"""

# from django.apps import AppConfig
 
# class UsersConfig(AppConfig):
#     name = 'users'
 
#     def ready(self):
#         import users.signals


from django.db import models
from django.dispatch import receiver
import os 

# Create your models here.
class IMAGE(models.Model):
    data=models.ImageField(upload_to='images/')


@receiver(models.signals.post_delete, sender=IMAGE)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.data:
        if os.path.isfile(instance.data.path):
            os.remove(instance.data.path)


@receiver(models.signals.pre_save, sender=IMAGE)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = sender.objects.get(pk=instance.pk).data 
    except sender.DoesNotExist:
        return False

    new_file = instance.data
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
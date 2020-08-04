from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


channel_layer = get_channel_layer()


class RecognizedText(models.Model):

    class Meta:
        verbose_name = 'Recognized Text'

    active = models.BooleanField(default=False)
    date = models.DateField(auto_now=True)
    text = models.TextField()

    def __str__(self):
        return f'Recognized "{self.text}" on {self.date}'


@receiver(post_save, sender=RecognizedText, dispatch_uid='recognized-text-saved')
def text_saved(sender, instance, **kwargs):
    async_to_sync(channel_layer.group_send)('broadcast',
        {
            'type': 'tablet.save',
            'object': instance,
        }
    )


@receiver(post_delete, sender=RecognizedText, dispatch_uid='recognized-text-deleted')
def text_deleted(sender, instance, **kwargs):
    async_to_sync(channel_layer.group_send)('broadcast',
        {
            'type': 'tablet.delete',
            'object': instance,
        }
    )

"""
Module for products signals: post delete for images
"""

import os
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.conf import settings
import cloudinary.uploader
from products.models import Album


@receiver(post_delete, sender=Album)
def delete_album_image(sender, instance, **kwargs):
    """
    Signal called to Delete images after delete function
    called, images deleted from Media and Cloudinary
    """
    if instance.image and instance.image.name:
        # Prepare path in local filesystem
        image_path = (
            instance.image.name.split("media/", 1)[1].rsplit("_", 1)[0]
            + ".jpg"
        )
        full_path = os.path.join(settings.MEDIA_ROOT, image_path)
        # Check if the file exists before trying to remove it
        if os.path.exists(full_path):
            os.remove(full_path)
        # Delete from Cloudinary
        public_id = os.path.splitext(instance.image.name)[0]

        cloudinary.uploader.destroy(public_id)

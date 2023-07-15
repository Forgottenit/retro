import os
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.conf import settings
import cloudinary.uploader
from products.models import Album, Artist, Track


@receiver(pre_delete, sender=Album)
def delete_album_image(sender, instance, **kwargs):
    if instance.image and instance.image.name:
        print("IMAGE REMOVAL")
        # Prepare path in local filesystem
        image_path = (
            instance.image.name.split("media/", 1)[1].rsplit("_", 1)[0]
            + ".jpg"
        )
        full_path = os.path.join(settings.MEDIA_ROOT, image_path)
        # Check if the file exists before trying to remove it
        if full_path:
            print("IS FILE")
            os.remove(full_path)
        else:
            print(f"No file found at: {full_path}")

        # Delete from Cloudinary
        public_id = os.path.splitext(instance.image.name)[0]
        print("PUBLIC ID:", public_id)
        cloudinary.uploader.destroy(public_id)


@receiver(pre_delete, sender=Artist)
def delete_related_albums(sender, instance, **kwargs):
    albums_to_delete = instance.albums.all()
    for album in albums_to_delete:
        album.artists.remove(instance)

        if album.artists.count() == 0:
            album.delete()


@receiver(pre_delete, sender=Track)
def pre_delete_track(sender, instance, **kwargs):
    if instance.external_urls:
        external_url = instance.external_urls
        instance.external_urls = None
        instance.save()
        external_url.delete()


@receiver(pre_delete, sender=Artist)
def pre_delete_artist(sender, instance, **kwargs):
    if instance.external_urls:
        external_url = instance.external_urls
        instance.external_urls = None
        instance.save()
        external_url.delete()

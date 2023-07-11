from django.db.models.signals import pre_delete
from django.dispatch import receiver
from products.models import Album, Artist, Track
import os
import cloudinary.uploader
from django.conf import settings


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
    # Get all albums associated with this artist
    albums_to_delete = instance.albums.all()
    for album in albums_to_delete:
        # Need to remove the artist from the album before deleting to prevent recursion
        album.artists.remove(instance)
        # Check if this album has other artists associated, if not, delete it
        if album.artists.count() == 0:
            album.delete()


@receiver(pre_delete, sender=Track)
def pre_delete_track(sender, instance, **kwargs):
    # If this track has an associated ExternalUrl
    if instance.external_urls:
        external_url = instance.external_urls
        instance.external_urls = None  # nullify the relationship
        instance.save()  # save the track to update the foreign key
        external_url.delete()  # then delete the ExternalUrl


@receiver(pre_delete, sender=Artist)
def pre_delete_artist(sender, instance, **kwargs):
    # If this track has an associated ExternalUrl
    if instance.external_urls:
        external_url = instance.external_urls
        instance.external_urls = None  # nullify the relationship
        instance.save()  # save the track to update the foreign key
        external_url.delete()  # then delete the ExternalUrl

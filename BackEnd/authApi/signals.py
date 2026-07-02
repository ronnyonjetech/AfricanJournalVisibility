from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group

from .models import NewUser


@receiver(post_save, sender=NewUser)
def assign_author_group(sender, instance, created, **kwargs):
    print("SIGNAL FIRED")  # <-- add this
    if created:
        author_group, _ = Group.objects.get_or_create(
            name="Author"
        )

        instance.groups.add(author_group)